# 0001: The core is adapter-agnostic

## Context

The first version of an AI system usually imports one provider SDK directly. That is fast until the provider changes pricing, limits, or API shape.

## Decision

The core imports contracts, not vendor SDKs. Model and platform calls live in adapters. The core asks for a capability and receives a result.

## Consequences

- A provider change is an adapter change, not a rewrite.
- The core is testable with fake adapters.
- Some provider-specific features are harder to express. They become capability flags or adapter options, not core branches.
- The composition root must do more wiring.
