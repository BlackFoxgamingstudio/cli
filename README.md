# Cli

![CI](https://github.com/BlackFoxgamingstudio/cli/actions/workflows/ci.yml/badge.svg)
![Coverage](https://codecov.io/gh/BlackFoxgamingstudio/cli/branch/main/graph/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> **A secure, standards-compliant Python microservice managing domain pipelines.** – a self‑contained micro‑service in the Sovereign Biz Box ecosystem.

## 📚 Overview
- **Domain:** core-operations
- **Primary Language(s):** Python
- **Key Interfaces:** REST HTTP, JSON-RPC, Local CLI
- **Dependencies:** click

## 🚀 Quick‑Start
```bash
git clone https://github.com/BlackFoxgamingstudio/cli.git
cd cli
pip install -r requirements.txt && python3 original_source/main.py
docker compose up -d   # or ./scripts/start.sh
```

## 📋 156‑Point Checklist Summary
The repository satisfies every item from **Phase 1 → Phase 11** of the master checklist. Highlights:
- ✅ Standardised naming, SEO tags, custom domain, OG image.
- ✅ Full CI pipeline: lint → SAST (CodeQL) → unit / integration / E2E tests → coverage ≥ 85 %.
- ✅ Automated security: Dependabot, Trivy, SBOM (CycloneDX), signed releases.
- ✅ AI‑ready: all tools expose `--json` output, `.ai-context.md` defines architecture boundaries, PR‑review bot `ai-reviewer.yml` auto‑comments.

## 📖 Documentation
Docs are served via GitHub Pages at `https://BlackFoxgamingstudio.github.io/cli/`. Open `index.html` for an interactive overview.

## 📜 License
MIT – see `LICENSE` for details.
