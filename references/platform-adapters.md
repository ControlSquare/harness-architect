# Platform adapters

Platform adapters connect the core to the outside world: publishing, storage, images, and search.

They are where credentials and platform quirks live. They are not where business rules live.

## Kinds

| Kind | Operations | Example |
| --- | --- | --- |
| Publishing | create draft, update draft, publish, fetch, list | Substack, WordPress, a custom CMS |
| Storage | put, get, list, sign URL | S3, local disk |
| Images | generate, resize, convert, upload | an image model, a CDN |
| Search | query, fetch, index | a search API, a local index |

## Required behavior

Every adapter:

1. Returns a stable external ID for each write.
2. Accepts an idempotency key.
3. Distinguishes success, retryable failure, and permanent failure.
4. Redacts secrets from errors.
5. Supports a dry run where the operation allows it.

## Idempotency

Publishing is the dangerous one. A retry must not create a second post.

Use a key derived from the canonical slug and the content hash. If the platform has no idempotency support, the adapter stores a local mapping:

```json
{
  "slug": "example",
  "content_hash": "sha256:...",
  "external_id": "12345",
  "status": "draft"
}
```

## Auth

Credentials live in the adapter's environment or secret store. They never enter the core, a skill manifest, or a log line.

The adapter exposes capabilities, not credentials.

## Schema changes

Platforms change. A field rename should fail a contract test, not silently drop a value.

Keep a small round-trip test: create, fetch, compare canonical fields.

## Dry run

A dry run returns the intended operation and the payload. It does not call the platform unless the platform supports a true draft.

This is how the core is tested without publishing anything.

## Example

[examples/adapter.substack.json](../examples/adapter.substack.json) is an illustrative manifest. It is not a claim that every Substack operation is interchangeable with another platform.
