# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a personal knowledge base — a curated collection of technical notes, study materials, and resource links organized as Markdown files. There is no application code, build system, or test suite.

## Structure

Content is organized by topic area into top-level directories:

- **Books/** — Chapter-by-chapter notes on technical books (Database Internals, DDIA, Observability Engineering, Prometheus, Linux Command Line)
- **backend/** — Backend engineering notes and course materials (OS fundamentals, NGINX, ClickHouse, backend patterns)
- **programming/** — Language-specific resources (Go, Python, Rust)
- **system-design/** — System design topics (backend, infra, Kafka, distributed systems)
- **devops/** — DevOps tooling notes (Kubernetes/CKAD/CKS/KCSA, Helm, Terraform, containers, AWS ML Engineer Associate)
- **AI/** — AI/ML blogs and videos, plus Claude Code notes, context-graph/Neo4j fundamentals, and Agentic AI course modules
- **cloud/** — Cloud platform resources
- **linux/** — Linux resources
- **content/** — Miscellaneous (career planning, JS basics, security)

Within each directory, content is typically split into `blogs.md`, `videos.md`, `courses.md`, and topic-specific notes files.

## Conventions

- All content is Markdown (`.md`). Exceptions: a Cilium network policy YAML under `devops/kubernetes/CKS/Cillium/`, and supporting images (book covers, screenshots) alongside notes in `Books/`.
- File and directory names use mixed casing — some use Title Case with spaces, others use lowercase with hyphens. Match the existing convention of the parent directory when adding new files.
- Course notes are typically stored under a `courses/` subdirectory within the relevant topic, with a `README.md` as the course index.
- Resource link files (`blogs.md`, `videos.md`) collect curated external links with brief descriptions.

