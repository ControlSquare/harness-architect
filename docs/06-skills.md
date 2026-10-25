# Skills

A skill is one capability with a contract. It is not a prompt and it is not a vendor integration.

## Manifest

See [contracts/skill.schema.json](../contracts/skill.schema.json).

A skill declares:

- what it does
- what it needs
- what it returns
- what it is allowed to touch
- how it fails

## Permissions

Permissions are scoped capabilities:

- `files:read`
- `files:write`
- `network:read`
- `publish:draft`
- `images:generate`

A skill never receives raw credentials. The core passes only the capabilities the skill declares.

## Outputs

A skill returns paths, not payloads:

```json
{
  "brief_path": "data/notes/example.md",
  "source_count": 7
}
```

The next step reads the file if it needs the content. This keeps the context small and the handoff reviewable.

## Failure policy

Each skill declares one of:

- `stop`: the pipeline stops.
- `retry`: retry within the budget.
- `fallback`: try the declared fallback.
- `human`: put the work in the review queue.

A skill that silently returns a partial result is a bug.

## Lifecycle

1. Draft the manifest and contract.
2. Run the contract tests with a fake adapter.
3. Shadow-run on real inputs without publishing.
4. Activate for one workflow.
5. Deprecate with a major version note.

## Tests

Every skill lists its tests in the manifest. At minimum:

- happy path returns the declared outputs
- missing input fails with a useful error
- permission violation fails
- failure policy is honored

## Versioning

A skill version is part of the contract. A prompt change that changes behavior is a minor or major change, not a patch.
