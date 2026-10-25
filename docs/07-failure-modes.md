# Failure modes

Every automated system has failure modes. The architecture names them so the response is a design decision, not a surprise.

| Failure | Detection | Response | Owner |
| --- | --- | --- | --- |
| Model invents a fact | Claim has no source | Stop, mark missing, human review | Guardrail |
| Source disappears | Fetch returns 404 or changed hash | Stop, keep the claim flagged | Adapter |
| Voice drifts | Baseline comparison fails | Return errors, do not rewrite | Guardrail |
| Context is truncated | Token budget hit | Stop, split the task | Core |
| Tool call is malformed | Schema validation fails | Retry once, then fallback | Adapter |
| Platform schema changes | Round-trip contract test fails | Disable the adapter, alert | Platform adapter |
| Duplicate publish | Idempotency key mismatch | Return existing external ID | Platform adapter |
| Rate limit | 429 or provider error | Backoff within budget | Adapter |
| Partial write | Fetch does not match write | Mark unknown, do not retry blindly | Platform adapter |
| Guard bypass | A publish path skips the gate | Block release, contract test | Core |

## Response patterns

### Stop

The default for a quality failure. A missing source, a failed check, or an unknown publish state stops the run.

### Retry

Only for transient failures: rate limits, timeouts, a temporary network error. Retries use the same idempotency key.

### Fallback

A different adapter or model, within the same budget. A fallback is not permission to ignore the original failure; it is logged.

### Human

The work goes to the review queue with the errors attached. The reviewer sees what failed, not a rewritten piece.

## Quarantine

An adapter that fails its contract test is quarantined:

- removed from the composition root
- excluded from fallbacks
- surfaced in the run record

A quarantined adapter does not get a silent retry loop.

## The rule

If the system cannot prove a step succeeded, it reports failure. It does not guess, and it does not publish.
