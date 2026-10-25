# Harness Architect

An agent skill that designs an AI harness workspace from a business process, or restructures an existing folder or repo into one.

> The folder structure carries the harness. The core owns the work. Models and platforms are replaceable edges.

This is a specialization of [Interpretable Context Methodology](https://github.com/RinDig/icm-architect) (ICM, MIT). ICM designs any process. Harness Architect designs the AI layer around one: package boundaries, adapter contracts, skills, guardrails, and the single human decision.

## Install

Keep the folder named `harness-architect`. A skill's name must match its folder.

| Agent | Folder |
| --- | --- |
| Codex | `~/.agents/skills/` or `.agents/skills/` in a repo |
| Gemini CLI | `~/.gemini/skills/` or `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` or `.claude/skills/` |
| Claude apps | zip the folder and upload it under Customize, Skills |
| Cursor, Copilot, other Agent Skills clients | that client's skills folder |
| Any other agent | give it the folder, or paste `SKILL.md` and the files it points to |

Then ask: "design a publishing harness", "structure this workflow for agents", or "audit this automation".

## What it does

**Build mode.** It extracts the stages, checks, and stable rules from how the owner describes the work, then scaffolds the smallest workspace that carries them.

**Restructure mode.** It audits an existing folder, classifies files, finds what points at each one, and proposes a migration map before changing anything.

Every stage ends at a check. Every workspace passes a walk test: an agent with no memory can orient, act, and report status from the files alone.

## Forms

| Form | Use when |
| --- | --- |
| Publishing harness | Content is produced and published on a cadence |
| Research harness | The output is a sourced argument |
| Operations harness | A recurring internal workflow needs state |
| Agent-readable site | A site must serve people and AI tools |
| Custom | Name the stages yourself |

The forms are recipes over three primitives: a sequence of numbered stages, a shelf of same-shaped files, and a catalog that points down.

## Output tree

```text
workspace/
  AGENTS.md
  01_intake/
    CONTEXT.md
  02_map/
    CONTEXT.md
  03_contracts/
    CONTEXT.md
  04_verify/
    CONTEXT.md
  _templates/
  _tools/
```

Delete a stage you do not need. Add one only if it has a real output and a check.

## Quick start

1. Read [SKILL.md](SKILL.md).
2. Copy [assets/templates/AGENTS.md](assets/templates/AGENTS.md) and [assets/templates/stage-CONTEXT.md](assets/templates/stage-CONTEXT.md).
3. Fill [assets/templates/harness-spec.md](assets/templates/harness-spec.md).
4. Add contracts from [contracts/](contracts/).
5. Validate:

```bash
python scripts/check_workspace.py examples/workspace
python scripts/check_contracts.py
```

The example workspace is [examples/workspace](examples/workspace).

## What makes it different

ICM is general. This skill adds the parts an AI harness needs:

- package boundaries between core, skills, adapters, and guardrails
- contracts for harness and platform adapters
- content-degradation controls
- failure modes and run records
- one human decision before publish or send

It is design-first. It does not ship a model, a publishing client, or client data. The runnable example is [token-frugal-harness](https://github.com/ControlSquare/token-frugal-harness).

## Repository map

```text
SKILL.md              the method
references/           the detail, read only when a step needs it
assets/templates/     blank starters a workspace copies
contracts/            JSON schemas for skills and adapters
examples/workspace/   a minimal harness that passes the checks
scripts/              link, workspace, and contract checks
tests/                tests for the checks
```

## Related

- [ICM Architect](https://github.com/RinDig/icm-architect)
- [Interpretable Context Methodology paper](https://arxiv.org/abs/2603.16021)
- [Token-frugal reference implementation](https://github.com/ControlSquare/token-frugal-harness)
- [AI publishing case study](https://controlsquare.com/work/ai-publishing-harness)
- [AI automation at Control Square](https://controlsquare.com/ai-automation)
- [Work](https://controlsquare.com/work/)

## License

MIT. See [LICENSE](LICENSE).
