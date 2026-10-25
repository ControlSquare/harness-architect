# 0002: Files are the state boundary

## Context

Pipeline state kept in a conversation disappears when the session ends, and it grows the context on every turn.

## Decision

Queues, drafts, archives, run records, and progress live in files. Agents return paths. The next step reads the file.

## Consequences

- State survives restarts and machine changes.
- The handoff is inspectable and diffable.
- Files need naming, locking, and cleanup rules.
- A file is not a database. High-concurrency workflows need a real store, behind the same boundary.
