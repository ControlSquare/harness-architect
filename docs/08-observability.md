# Observability

A run should be reconstructable without reading a chat log.

## Run record

Write one JSON record per run:

```json
{
  "run_id": "2026-10-24T12-00-00Z-example",
  "workflow": "publish-draft",
  "skill": "research-brief@1.0.0",
  "adapters": ["harness:primary", "platform:substack"],
  "budget": {"input_tokens": 40000, "output_tokens": 4000},
  "usage": {"input_tokens": 18200, "output_tokens": 900},
  "status": "human_review",
  "guard_failures": [],
  "artifacts": ["data/drafts/example.md"],
  "started_at": "2026-10-24T12:00:00Z",
  "finished_at": "2026-10-24T12:03:12Z"
}
```

## Rules

- **No secrets.** Redact tokens, cookies, API keys, and session IDs before writing.
- **No full content by default.** Record paths and hashes, not the whole draft.
- **One status per run.** `ok`, `human_review`, `failed`, `quarantined`.
- **Cost is a metric.** Record usage even when the provider does not bill per token.
- **Review edits are data.** Count them. They show where the mechanical layer fails.

## Metrics

| Metric | Why |
| --- | --- |
| Guard failures per run | Shows quality drift |
| Review edits per piece | Shows where the gate is weak |
| Tokens and cost per piece | Shows whether the system is sustainable |
| Time to review | Shows whether the human step is bounded |
| Rework after publish | Shows whether the gate missed something |

## Alerts

Alert on:

- three consecutive guard failures for the same check
- an adapter contract test failure
- a run that exceeds budget
- a publish with an unknown external state
- a queue item older than its review window

Alerts go to a human. They do not trigger an automatic retry storm.

## What not to log

- credentials or session cookies
- full source text
- private subscriber data
- unpublished client content

The run record is evidence, not a copy of the work.
