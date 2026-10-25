# Content degradation

Content degradation is the slow loss of quality that happens when automation is measured by output volume instead of trust.

It is not a style preference. It is a failure mode.

## Common failure modes

| Failure | What it looks like | First control |
| --- | --- | --- |
| Unsupported claim | A confident sentence with no source | Claim-to-source map |
| Stale source | A 2023 number presented as current | Source date and retrieval date |
| Voice drift | The piece sounds like a different publication | Voice baseline and diff |
| Structure loss | Headings, tables, or lists flatten | Structural checks |
| Silent truncation | The end of a long input disappears | Budget and length checks |
| Over-automation | A model decides what should be human | Review gate |
| Formatting damage | A publish step changes emphasis or links | Round-trip test |

## Controls

### Source capture

Every factual claim carries a source, a date, and a retrieval date. Missing sources stay visible. They are not filled with a plausible guess.

### Claim map

The draft links each claim to a source. If the source disappears, the claim fails the gate.

### Voice baseline

The publication has a measured baseline. Drift is detected by comparing the draft to it, not by asking the model whether it sounds right.

### Structure checks

Headings, links, lists, tables, images, and captions are checked before review. A publish adapter is not allowed to be the first place a structure is tested.

### Human review

One person reviews the argument, the voice, and whether the piece is worth publishing. The reviewer sees errors, not a rewritten draft.

### Regression suite

A sample of past pieces runs through the gate after every change. A new check that breaks old work is a regression, not progress.

## The self-review trap

A model cannot be the only judge of its own output. It shares the same blind spots that produced the draft.

Use deterministic checks for mechanics, a human for judgment, and a separate review pass for sourcing. The separation matters more than the model.

## Metrics

Track:

- guard failures per run
- review edits per piece
- unsupported claims caught
- time from draft to review
- rework rate after publish

The goal is not zero edits. The goal is that a reviewer spends time on the argument, not on fixing the same mechanical failure every week.
