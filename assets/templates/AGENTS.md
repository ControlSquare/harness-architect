# <Harness name>

<One sentence: what this harness does, and where the human decides.>

## Where am I

Root of the harness workspace. State lives in files, not in a chat.

## Rules

- Read only the stage you are working in.
- Every stage has a `CONTEXT.md`.
- Every stage ends at a check. A fail stops the run.
- No credentials, client content, or session data in this workspace.
- One home per fact. Link, do not copy.

## Map

| Stage | Purpose | Output |
| --- | --- | --- |
| [01_intake](01_intake/CONTEXT.md) | Capture the process and the owner | intake.md |
| [02_map](02_map/CONTEXT.md) | Name the boundaries, adapters, and skills | harness-spec.md |
| [03_contracts](03_contracts/CONTEXT.md) | Write the manifests and checks | contracts/ |
| [04_verify](04_verify/CONTEXT.md) | Run the walk test | check.md |

## Start here

- New harness: read `01_intake/CONTEXT.md`.
- Existing harness: read `04_verify/CONTEXT.md` and run the check.
- The human decision: <who decides, and what they decide.>

## References

- Architecture: `_references/` or the skills library.
- Templates: `_templates/`.
- Tools: `_tools/`.
