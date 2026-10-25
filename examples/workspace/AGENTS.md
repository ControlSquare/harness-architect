# Example publishing harness

A small harness that turns a topic into a reviewed draft. The publisher makes the publish decision.

## Where am I

Root of the harness workspace. State lives in files.

## Rules

- Read only the stage you are working in.
- Every stage has a `CONTEXT.md`.
- A failed check stops the run.
- No credentials or client content here.

## Map

| Stage | Purpose | Output |
| --- | --- | --- |
| [01_intake](01_intake/CONTEXT.md) | Capture the topic, owner, and decision | intake.md |
| [02_map](02_map/CONTEXT.md) | Name boundaries, adapters, and skills | harness-spec.md |
| [03_contracts](03_contracts/CONTEXT.md) | Write manifests and checks | contracts/ |
| [04_verify](04_verify/CONTEXT.md) | Run the walk test | check.md |

## Start here

- New harness: read `01_intake/CONTEXT.md`.
- Existing harness: read `04_verify/CONTEXT.md`.
- Human decision: the publisher approves the draft. Publishing is a separate action.

## References

- [Harness spec](02_map/harness-spec.md)
- [Guardrail policy](03_contracts/guardrail-policy.yaml)
