# UltraJarvis_v8 — Grok working copy

Self-upgrading Python agent pipeline.

**Continuity:** read `docs/GROK_CONTINUITY.md` and `taskgrok.md` first.

## Quick start

```bash
python -m pytest -q
python bin/uj health
python bin/uj tools
python bin/uj seed "Add a helper function"
python bin/uj run --all
python bin/uj snapshot
```

## Pipeline

Architect → Write → Gates → Critic → Safety → Verify

## Status (2026-08-17)

- Phase 1 complete (tools, registry, gates, metrics, CLI)
- Phase 2 starters (memory, critic, safety advisors)
- **76 tests** green

Original upstream: [mootmoot1/UltraJarvis_v8](https://github.com/mootmoot1/UltraJarvis_v8)
