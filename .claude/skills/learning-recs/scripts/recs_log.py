#!/usr/bin/env python3
"""Helper for the learning-recs skill: taste profile, dedupe, suggestion log.

Stdlib only. All subcommands print JSON to stdout.

  profile                 Summarise the repo: topics, recent activity, trusted
                          domains, recently saved titles, past feedback.
  check  --file F         Classify candidate items as new / duplicate.
  add    --file F         Append picks to the log (duplicates are refused).
  mark   ID --status S    Record feedback: suggested | saved | skipped.
  commit                  git add + commit the log file only.

The repo is found from --repo, $TECH_CONTENTS_REPO, the script's own location,
or the current directory (first one that is inside a git repo).
The log lives at <repo>/learning-log/suggestions.json.
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from collections import Counter
from urllib.parse import parse_qs, urlsplit

LOG_REL = "learning-log/suggestions.json"
SKIP_DIRS = {".git", ".idea", ".remember", ".claude", "learning-log", "skills", "node_modules"}
URL_RE = re.compile(r"https?://[^\s)>\]\"']+")
# [title](url) and the repo's occasional reversed (title)[url]
LINK_RE = re.compile(r"[\[(]([^\]\[()]{3,200})[\])][\[(](https?://[^\s)\]]+)[\])]")
TRACKING = re.compile(r"^(utm_.*|si|t|list|index|app|feature|ref|source|pp|ab_channel|fbclid|gclid|sk)$")
REPO = None


def find_git_root(start):
    d = os.path.abspath(start)
    while True:
        if os.path.exists(os.path.join(d, ".git")):
            return d
        if d == os.path.dirname(d):
            return None
        d = os.path.dirname(d)


def repo_root():
    starts = [REPO, os.environ.get("TECH_CONTENTS_REPO"),
              os.path.dirname(os.path.abspath(__file__)), os.getcwd()]
    for s in starts:
        if s:
            root = find_git_root(s)
            if root:
                return root
    sys.exit(json.dumps({"error": "tech-contents repo not found; pass --repo <path>"}))


def norm_url(url):
    """Canonical key for a URL so the same content always maps to one id."""
    url = url.strip().rstrip(".,;")
    p = urlsplit(url)
    host = p.netloc.lower()
    for pre in ("www.", "m.", "mobile."):
        if host.startswith(pre):
            host = host[len(pre):]
    path = p.path.rstrip("/")
    q = parse_qs(p.query)
    if host == "youtu.be" and path.strip("/"):
        return "yt:" + path.strip("/").split("/")[0]
    if host in ("youtube.com", "music.youtube.com", "youtube-nocookie.com"):
        if "v" in q:
            return "yt:" + q["v"][0]
        m = re.match(r"^/(?:shorts|embed|live)/([\w-]+)", path)
        if m:
            return "yt:" + m.group(1)
        if path == "/playlist" and "list" in q:
            return "ytlist:" + q["list"][0]
    kept = sorted((k, v[0]) for k, v in q.items() if not TRACKING.match(k.lower()))
    qs = "?" + "&".join(f"{k}={v}" for k, v in kept) if kept else ""
    return host + path.lower() + qs


def norm_title(title):
    t = re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()
    return t if len(t) >= 12 else ""  # short titles collide too easily


def md_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.lower().endswith(".md"):
                yield os.path.join(dirpath, f)


def scan_repo(root):
    """Everything already saved in the notes: url ids, titles, per-area stats."""
    ids, titles, domains, areas = {}, {}, Counter(), Counter()
    for path in md_files(root):
        rel = os.path.relpath(path, root)
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        area = "/".join(rel.split(os.sep)[:2]) if os.sep in rel else rel
        for u in URL_RE.findall(text):
            k = norm_url(u)
            ids.setdefault(k, rel)
            areas[area] += 1
            if not k.startswith("yt"):
                domains[k.split("/")[0].split("?")[0]] += 1
        for title, u in LINK_RE.findall(text):
            nt = norm_title(title)
            if nt and not title.startswith("http"):
                titles.setdefault(nt, rel)
    return ids, titles, domains, areas


def load_log(root):
    path = os.path.join(root, LOG_REL)
    if not os.path.exists(path):
        return {"version": 1, "suggestions": []}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("suggestions", [])
    return data


def save_log(root, data):
    path = os.path.join(root, LOG_REL)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def git(root, *args):
    r = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def read_items(path):
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    items = json.loads(raw)
    if isinstance(items, dict):
        items = items.get("items") or items.get("suggestions") or [items]
    return items


def classify(items, root):
    """Return (new, dupes, log). Dedupes against notes, the log, and the batch."""
    ids, titles, _, _ = scan_repo(root)
    log = load_log(root)
    log_ids = {s["id"]: s for s in log["suggestions"]}
    log_titles = {norm_title(s.get("title")): s for s in log["suggestions"]}
    log_titles.pop("", None)
    seen, new, dupes = set(), [], []
    for it in items:
        url = it.get("url", "")
        if not url:
            dupes.append({**it, "reason": "missing url"})
            continue
        k, nt = norm_url(url), norm_title(it.get("title"))
        reason = None
        if k in ids:
            reason = f"already in notes: {ids[k]}"
        elif k in log_ids:
            reason = f"already suggested on {log_ids[k].get('suggested_on')}"
        elif nt and nt in titles:
            reason = f"same title already in notes: {titles[nt]}"
        elif nt and nt in log_titles:
            reason = f"same title already suggested on {log_titles[nt].get('suggested_on')}"
        elif k in seen or (nt and nt in seen):
            reason = "repeated within this batch"
        if reason:
            dupes.append({"url": url, "title": it.get("title"), "reason": reason})
        else:
            seen.add(k)
            if nt:
                seen.add(nt)
            new.append({**it, "id": k})
    return new, dupes, log


def cmd_profile(a):
    root = repo_root()
    ids, _, domains, areas = scan_repo(root)
    log = load_log(root)
    # What has been touched lately says more about current interest than totals.
    since = f"--since={a.days} days ago"
    rc, out = git(root, "log", since, "--name-only", "--format=")
    recent = Counter(
        l for l in out.splitlines()
        if rc == 0 and l.endswith(".md") and not l.startswith((".claude", "learning-log", "skills"))
    )
    rc, out = git(root, "log", since, "-p", "--format=", "--", "*.md")
    added = []
    if rc == 0:
        for line in out.splitlines():
            if line.startswith("+") and not line.startswith("+++"):
                for title, _u in LINK_RE.findall(line):
                    if not title.startswith("http"):
                        added.append(title.strip())
    rc, out = git(root, "log", "-8", "--format=%cs %s")
    sug = log["suggestions"]

    def fb(status):
        return [{k: s.get(k) for k in ("title", "source", "topic", "note") if s.get(k)}
                for s in sug if s.get("status") == status][-15:]

    print(json.dumps({
        "repo": root,
        "today": dt.date.today().isoformat(),
        "links_in_notes": len(ids),
        "links_by_area": areas.most_common(25),
        f"files_touched_last_{a.days}d": recent.most_common(20),
        f"titles_saved_last_{a.days}d": list(dict.fromkeys(added))[-60:],
        "recent_commits": out.splitlines() if rc == 0 else [],
        "trusted_domains_from_notes": domains.most_common(40),
        "log": {
            "total": len(sug),
            "by_status": dict(Counter(s.get("status", "suggested") for s in sug)),
            "last_run": max((s.get("suggested_on", "") for s in sug), default=None),
            "recent_suggestions": [
                {k: s.get(k) for k in ("title", "source", "topic", "suggested_on")} for s in sug[-15:]
            ],
            "liked_saved": fb("saved"),
            "skipped": fb("skipped"),
        },
    }, ensure_ascii=False))


def cmd_check(a):
    new, dupes, _ = classify(read_items(a.file), repo_root())
    print(json.dumps({"new": new, "duplicates": dupes}, indent=1, ensure_ascii=False))


def cmd_add(a):
    root = repo_root()
    new, refused, log = classify(read_items(a.file), root)
    today = dt.date.today().isoformat()
    added = []
    for it in new:
        missing = [f for f in ("title", "url", "type") if not it.get(f)]
        if missing:
            refused.append({"url": it.get("url"), "reason": "missing " + ",".join(missing)})
            continue
        entry = {
            "id": it["id"],
            "title": it["title"].strip(),
            "url": it["url"].strip(),
            "type": it["type"],
            "source": it.get("source", ""),
            "topic": it.get("topic", ""),
            "published": it.get("published", ""),
            "why": it.get("why", ""),
            "suggested_on": today,
            "status": "suggested",
        }
        log["suggestions"].append(entry)
        added.append(entry)
    if added:
        save_log(root, log)
    print(json.dumps({"added": added, "refused": refused, "log": LOG_REL,
                      "total": len(log["suggestions"])}, indent=1, ensure_ascii=False))


def cmd_mark(a):
    root = repo_root()
    log = load_log(root)
    key = norm_url(a.id) if a.id.startswith("http") else a.id
    hits = [s for s in log["suggestions"]
            if s["id"] == key or a.id.lower() in s.get("title", "").lower()]
    if len(hits) != 1:
        print(json.dumps({"error": f"{len(hits)} matches for {a.id!r}",
                          "matches": [s["title"] for s in hits]}))
        sys.exit(1)
    hits[0]["status"] = a.status
    if a.note:
        hits[0]["note"] = a.note
    save_log(root, log)
    print(json.dumps({"updated": hits[0]}, indent=1, ensure_ascii=False))


def cmd_commit(a):
    root = repo_root()
    rc, out = git(root, "status", "--porcelain", "--", LOG_REL)
    if rc != 0:
        print(json.dumps({"committed": False, "error": out}))
        sys.exit(1)
    if not out:
        print(json.dumps({"committed": False, "reason": "log unchanged"}))
        return
    msg = a.message or f"learning-log: suggestions for {dt.date.today().isoformat()}"
    rc, out = git(root, "add", "--", LOG_REL)
    if rc == 0:
        # Pathspec keeps any other staged or unstaged work out of this commit.
        rc, out = git(root, "commit", "-m", msg, "--", LOG_REL)
    if rc != 0:
        print(json.dumps({"committed": False, "error": out,
                          "hint": f"log is written; commit by hand: git add {LOG_REL} && git commit -m \"{msg}\""}))
        sys.exit(1)
    _, sha = git(root, "rev-parse", "--short", "HEAD")
    print(json.dumps({"committed": True, "commit": sha, "message": msg, "pushed": False}))


def main():
    global REPO
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", help="path to the tech-contents repo")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("profile")
    p.add_argument("--days", type=int, default=90)
    p.set_defaults(fn=cmd_profile)
    p = sub.add_parser("check")
    p.add_argument("--file", required=True)
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser("add")
    p.add_argument("--file", required=True)
    p.set_defaults(fn=cmd_add)
    p = sub.add_parser("mark")
    p.add_argument("id")
    p.add_argument("--status", required=True, choices=["suggested", "saved", "skipped"])
    p.add_argument("--note")
    p.set_defaults(fn=cmd_mark)
    p = sub.add_parser("commit")
    p.add_argument("--message")
    p.set_defaults(fn=cmd_commit)
    a = ap.parse_args()
    REPO = a.repo
    a.fn(a)


if __name__ == "__main__":
    main()
