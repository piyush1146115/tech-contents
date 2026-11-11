---
name: learning-recs
description: Suggest fresh, credible tech blogs and videos tailored to Piyush's learning history in the tech-contents repo, without ever repeating something already saved or previously suggested, and log every suggestion to a JSON file committed in git. Use this whenever the user asks what to read, watch or learn next, wants learning content, blog or video recommendations, a reading/watch list, "what's new in <topic> worth my time", "suggest some learning contents", or gives feedback on earlier suggestions (liked, skipped, save it to my notes), even if they don't mention the repo or this skill by name.
---

# Learning recommendations

Recommend a small batch of recent, high-quality blogs and videos that fit what the user is studying, then record them so they are never suggested twice.

The `tech-contents` repo is the user's learning history: Markdown notes and curated link lists (`blogs.md`, `videos.md`, course and book notes) by topic. What is in it shows taste; what was committed recently shows current focus. The suggestion log at `learning-log/suggestions.json` in the same repo is the memory between runs.

All bookkeeping goes through `scripts/recs_log.py` (Python 3, stdlib only). It finds the repo from its own location; if the skill is installed elsewhere, pass `--repo <path to tech-contents>` before the subcommand or set `TECH_CONTENTS_REPO`. Use the script rather than editing the JSON by hand: it normalises URLs (YouTube IDs, tracking parameters, `www.`), which is what makes dedupe reliable.

## Workflow

### 1. Read the profile

```bash
python3 scripts/recs_log.py profile
```

This returns links per topic area, files touched and titles saved in the last 90 days, recent commit messages, the domains the user already trusts, and the log's recent suggestions plus anything marked `saved` (liked) or `skipped` (with notes). Open a notes file directly only if you need more texture on a topic, such as what level the user is at.

### 2. Decide what to look for

Honour anything the user specified: topic, blog vs video, count, time window. Otherwise default to **5 picks, mixing blogs and videos, published in roughly the last 30 days**, spread like this:

- about 3 from the current focus (areas with the most recent commits and saved titles)
- 1 or 2 from steady long-term interests that have been quiet lately
- at most 1 stretch pick: adjacent to their interests, something they would not have searched for

Let feedback steer: lean toward sources and topics marked `saved`, away from those marked `skipped`, and read the notes for the reason. Infer the level from the notes. Someone with chapter notes on Database Internals does not need "What is a database index?".

### 3. Research

Run searches in parallel, several angles per topic, the way a person who follows the field would:

- **Trusted sources first.** Check recent output from `trusted_domains_from_notes` and from `references/sources.md` (read that file now; it lists credible blogs, newsletters and channels per topic).
- **Community signal.** Hacker News is a good filter for engineering posts; the Algolia API is fetchable without a key, e.g. `https://hn.algolia.com/api/v1/search_by_date?query=postgres&tags=story&numericFilters=points>150,created_at_i><unix_ts>`. Curated newsletters and conference playlists (KubeCon, AI Engineer, GopherCon, P99 CONF, RustConf) work the same way.
- **Videos.** Search for recent talks and deep dives by channel or speaker name. Prefer conference talks, practitioner channels and lectures over reaction and news-recap videos.

Gather a pool of 15 to 25 candidates, since many will fall out. If 30 days is thin for a niche topic, widen to 90 days and say so. Older evergreen pieces are fine only when the user asks for them or as a clearly labelled exception.

### 4. Dedupe before investing in anything

Write the pool to a temp file as a JSON array of `{"title", "url", "type"}` and run:

```bash
python3 scripts/recs_log.py check --file /tmp/candidates.json
```

Drop everything under `duplicates`. That list covers links already in the notes, anything suggested before (whatever its status), and same-title reposts. Also drop near-duplicates the script cannot see: the same talk re-uploaded on another channel, a newsletter summary of a post already in the notes, or a third introduction to a topic the log shows was covered last week. Repetition is the main thing the user wants this skill to prevent, so when unsure, drop it.

### 5. Verify and choose

Open each finalist before recommending it. Confirm that the URL resolves, the title and author are what you think, and the publish date is real. Never recommend from a search snippet alone and never construct a URL from memory; a dead or wrong link costs the user more than a missing pick. If a page cannot be fetched (YouTube often cannot), rely on search results that show the exact URL, title, channel and date, and say the date is approximate if it is.

Credible means: written by someone who does the work (engineers at companies running the thing, maintainers, researchers, long-standing independent writers), specific and technical, original rather than a rewrite. Be sceptical of anonymous listicles, SEO content farms, vendor pieces that are mostly a product pitch, and clickbait titles. The user does save some Medium posts and vendor engineering blogs, so judge the piece, not the domain.

Rank on relevance to the profile, credibility, depth, freshness and community signal. Then balance the batch: no more than 2 picks from one source, at least 2 topic areas, a mix of formats, and a mix of time commitment where possible.

### 6. Present

Keep it scannable. For each pick:

```
**1. [Title](url)** · Blog · Author / Site · 2026-11-03 · ~12 min
Why you: one or two sentences tying it to something specific in the notes or recent activity.
```

Group or order by topic, lead with the strongest pick, and end with one line on what was skipped as already seen if that is informative (for example "3 strong candidates were already in your notes"). No long preamble.

### 7. Log and commit

Write the final picks to a temp file and add them. `title`, `url` and `type` (`blog` or `video`) are required; include the rest so the log stays useful for future taste decisions:

```json
[{"title": "...", "url": "https://...", "type": "blog",
  "source": "Author / Site or Channel", "topic": "AI/agents",
  "published": "2026-11-03", "why": "short reason"}]
```

```bash
python3 scripts/recs_log.py add --file /tmp/picks.json
python3 scripts/recs_log.py commit
```

`add` refuses duplicates as a final safety net; if it refuses one you already showed, tell the user and replace it. `commit` stages and commits only the log file, so other uncommitted work in the repo is left alone. It does not push; leave pushing to the user unless they ask. If the commit fails (for instance a sandbox that cannot write to `.git`), the log file is still updated: report the failure and give the user the one-line command from the `hint` field.

Finish with one line confirming the log entry and commit hash.

## Feedback and saving to notes

When the user reacts to earlier suggestions, record it. This is how taste improves over time:

```bash
python3 scripts/recs_log.py mark "<id, url, or unique part of the title>" --status skipped --note "too introductory"
python3 scripts/recs_log.py mark "<...>" --status saved
python3 scripts/recs_log.py commit --message "learning-log: feedback"
```

If the user asks to save a pick into their notes, append it to the matching `blogs.md` or `videos.md` for that topic, following that file's existing style (`- [Title](url)` with optional indented bullets for notes), then mark it `saved`. Do not add to the notes files unprompted; they are a record of what the user actually read.

## Log format

`learning-log/suggestions.json`:

```json
{"version": 1, "suggestions": [
  {"id": "yt:CEvIs9y1uog", "title": "...", "url": "...", "type": "video",
   "source": "...", "topic": "...", "published": "2026-11-03", "why": "...",
   "suggested_on": "2026-11-11", "status": "suggested"}
]}
```

`id` is the normalised URL key used for dedupe. `status` is `suggested`, `saved` or `skipped`, with an optional `note`.
