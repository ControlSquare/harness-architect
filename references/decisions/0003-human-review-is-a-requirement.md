# 0003: Human review is a requirement

## Context

It is technically possible to publish without review. It is also how a brand loses trust in one bad run.

## Decision

The pipeline stops before the publish decision. A human reviews the argument, the voice, and whether the piece is worth publishing.

The review is one decision, not a dashboard. Mechanical checks happen before it.

## Consequences

- The system cannot run fully unattended.
- The human step is bounded and meaningful.
- Publishing can later be scheduled after trust is established, but the review remains.
- The review record is part of the run history.
