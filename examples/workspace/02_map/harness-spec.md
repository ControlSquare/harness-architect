# Harness spec

## Process

Turn a topic into a reviewed draft.

## Owner and decision

- Owner: the publisher
- Decision: publish or not
- Publish: a human action

## Inputs

- topic
- audience

## Outputs

- reviewed draft

## Stages

| Stage | Reads | Writes | Check |
| --- | --- | --- | --- |
| 01_intake | AGENTS.md | intake.md | owner confirms |
| 02_map | intake.md | harness-spec.md | contracts exist |
| 03_contracts | harness-spec.md | manifests | schema passes |
| 04_verify | workspace | check.md | walk test |

## Adapters

- harness: one model adapter
- publishing: one draft adapter
- storage: one file store

## Skills

- research-brief: produces a sourced brief
- draft: produces a draft from the brief

## Guardrails

- sources
- structure
- voice
- human review
