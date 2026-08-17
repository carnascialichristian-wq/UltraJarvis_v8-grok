# UltraJarvis Developer Pipeline

Self-upgrade / job execution pipeline.

## Stages

```
Architect → Write → Gates → Critic → Verify
```

| Stage | Module | Notes |
|-------|--------|-------|
| Architect | `core.planner` | Plan dataclass + plan.md |
| Write | `core.natural_tasks` | Controlled writes under job dir |
| Gates | `core.gates` | ruff/black/pytest when installed |
| Critic | `advisors.critic` | Rule-based verdict |
| Verify | `core.verify` | PASS/FAIL + verify.txt |

## CLI

```bash
python bin/uj health
python bin/uj status
python bin/uj seed "Add a utility…"
python bin/uj run --all
python bin/uj tools [--tag …]
python bin/uj memory add "fact" --tag status
python bin/uj memory list
```

## Continuity

- `docs/GROK_CONTINUITY.md` + `taskgrok.md`

## Repo

- https://github.com/carnascialichristian-wq/UltraJarvis_v8-grok
