# Contracts

Contracts are how the core stays independent of models, skills, and platforms.

A contract is a schema plus a small set of rules. It is not a prompt, and it is not a vendor API.

## Skill contract

A skill manifest declares:

- `name` and `version`
- `description`
- `inputs` and `outputs`
- `permissions`
- `adapters` it requires
- `cost_class`
- `failure_policy`
- `tests`

The full schema is [contracts/skill.schema.json](../contracts/skill.schema.json).

A skill returns a **path**, not the full content. The caller reads the path if it needs the output. This keeps context small and makes the handoff inspectable.

## Adapter contract

A platform adapter declares:

- `name` and `version`
- `kind`: publishing, storage, images, or search
- `operations`
- `auth` style
- `idempotent`

The full schema is [contracts/platform-adapter.schema.json](../contracts/platform-adapter.schema.json).

An adapter must return a stable external ID for every write, or an explicit failure. It must never report success without one.

## Versioning

Use semantic versioning.

- Patch: bug fixes, no schema change.
- Minor: additive fields, no required change.
- Major: removed or renamed fields, changed meaning.

The core accepts a range of contract versions. Adapters and skills declare the range they implement.

## Contract tests

A contract test is not a unit test of one vendor. It is the same suite run against every implementation.

For a publishing adapter:

1. Create a draft twice with the same idempotency key.
2. Assert one external object.
3. Fetch it and compare the canonical fields.
4. Simulate a rate limit and assert the retry behavior.
5. Simulate a partial write and assert the failure is explicit.

For a harness adapter:

1. Return a structured result for a simple task.
2. Report usage.
3. Surface a provider error without leaking secrets.
4. Respect the token or time budget.
5. Declare unsupported capabilities instead of pretending.

## Breaking changes

A breaking contract change requires:

- a major version
- a migration note
- a compatibility window
- an update to the example manifests

If a change cannot be expressed in the contract, the design is probably hiding a vendor assumption in the core.
