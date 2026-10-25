---
name: harness-architect
description: Design an AI harness workspace from a business process, or restructure an existing folder or repo into one. Use for "design a harness", "structure this workflow for agents", "map this repo", "where does the AI go", "audit this automation", "make this maintainable", or a publishing, research, content-operation, or internal-tool harness.
license: MIT
---

# Harness Architect

Build a workspace where the folder structure carries the harness design. One agent, reading the right files at the right moment, does the work of a fragile multi-agent setup. A person can open any folder and see the state, because state is files.

This skill specializes [Interpretable Context Methodology](https://github.com/RinDig/icm-architect) (ICM, MIT) for AI harnesses. ICM designs any process. This designs the layer around an AI system: boundaries, adapters, contracts, skills, guardrails, and the one human decision. See [references/icm-lineage.md](references/icm-lineage.md).

## The invariants

1. **One folder, one job.** Each stage does one thing and states its purpose in its own `CONTEXT.md`.
2. **A small entry file.** `AGENTS.md` at the root answers where am I, where things live, and where to go next. It routes and stores no content.
3. **Numbering encodes order.** `01_`, `02_`, and so on, where sequence matters.
4. **Every stage has a contract.** `CONTEXT.md` lists what it reads, what it does, what it writes, and how it is checked.
5. **Factory vs product.** Stable rules and templates live apart from the artifacts each run produces.
6. **Every stage ends at a check.** A person, a script, or a small model. A fail stops the run there.
7. **Load only what the stage needs.** A stage reads its contract, its references, and its inputs. Not the whole workspace.
8. **Plain text, relative links.** Markdown and YAML. One home per fact. A link beats a copy.
9. **Status lives on disk.** What exists, or one status line in the file it describes. Generated indexes are rebuilt, not hand-edited.
10. **Instantiate by copying.** A new unit is a copy of a template, not a blank page.

## Choose a mode

- **Build**: from a described process, idea, or problem.
- **Restructure**: an existing folder, repo, or vault that needs a harness structure.

## Build mode

1. **Extract the process.** Ask for the stages, the inputs, the outputs, the checks, and the person who decides. The structure is usually already in how the owner describes the work.
2. **Choose the smallest form.** See [Forms](#forms). Do not build a stage that has no output or no check.
3. **Scaffold from templates.** Copy [assets/templates/AGENTS.md](assets/templates/AGENTS.md) and [assets/templates/stage-CONTEXT.md](assets/templates/stage-CONTEXT.md). Never start from a blank file.
4. **Write the harness spec.** Use [assets/templates/harness-spec.md](assets/templates/harness-spec.md). Name the owner, the decision, the inputs, the outputs, and the constraints.
5. **Define the edges.** List harness adapters, platform adapters, and skills. Give each a contract from [contracts/](contracts/).
6. **Define the guardrails.** Start from [assets/templates/guardrail-policy.yaml](assets/templates/guardrail-policy.yaml). Every stage must name its check.
7. **Validate.** Run `python scripts/check_workspace.py <workspace>` and `python scripts/check_contracts.py`.
8. **Run the walk test.** Then hand off.

## Restructure mode

1. **Audit the files.** Classify each as catalog, contract, factory, product, or dead.
2. **Find what points at each one.** A file with inbound links is harder to move than a leaf.
3. **Propose the migration map.** Show old path, new path, and the reason. Wait for approval.
4. **Copy, validate, then remove.** Do not move a file until its new home passes the link and workspace checks.
5. **Run the walk test.** The new structure is not done until an agent with no memory can orient.

## Forms

Each form is a recipe over three primitives: a sequence of numbered stages, a shelf of same-shaped files, and a catalog that points down.

| Form | Stages | Use when |
| --- | --- | --- |
| Publishing harness | intake, map, contracts, build, verify | Content is produced and published on a cadence |
| Research harness | question, sources, claims, brief, verify | The output is a sourced argument, not a draft |
| Operations harness | intake, map, build, monitor | A recurring internal workflow needs state |
| Agent-readable site | inventory, contracts, negotiation, verify | A site must serve people and AI tools |
| Custom | name the stages | Nothing above fits |

Nest forms only when each level has its own small catalog. Keep the top-level `AGENTS.md` under about 60 lines.

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
  04_build/
    CONTEXT.md
  05_verify/
    CONTEXT.md
  _templates/
  _tools/
```

Copy the templates. Delete a stage you do not need. Add one only if it has a real output and a check.

## Stage contract

Every `CONTEXT.md` has four sections:

```markdown
# 02_map

## Reads
- ../01_intake/CONTEXT.md
- ../01_intake/intake.md

## Does
1. Separate the judgment from the mechanical steps.
2. Name the adapters and skills.

## Writes
- harness-spec.md

## Check
A person confirms the owner and the decision. A script checks that every adapter has a contract.
```

A stage with no `## Check` is not a stage. It is a wish.

## The walk test

An agent with no memory must be able to:

1. Open `AGENTS.md` and orient.
2. Find the stage that matches the task.
3. Read only that stage's contract, references, and inputs.
4. Produce the declared output.
5. Run or name the check.
6. Report status from files.

If any of those needs a conversation history, the workspace failed.

## Guardrails

- No client data, credentials, or session cookies in the workspace.
- No vendor SDK in the core. Adapters own the vendor.
- One human decision before publish or send.
- Content checks run before a human review, not instead of it.
- A failed check stops the run. It does not trigger a silent retry storm.
- Missing facts stay missing.

## Templates

- [AGENTS.md](assets/templates/AGENTS.md)
- [stage-CONTEXT.md](assets/templates/stage-CONTEXT.md)
- [harness-spec.md](assets/templates/harness-spec.md)
- [skill-manifest.json](assets/templates/skill-manifest.json)
- [adapter-manifest.json](assets/templates/adapter-manifest.json)
- [guardrail-policy.yaml](assets/templates/guardrail-policy.yaml)

## References

Read only what the current step needs.

- [ICM lineage and difference](references/icm-lineage.md)
- [Package boundaries](references/package-boundaries.md)
- [Contracts](references/contracts.md)
- [Content degradation](references/content-degradation.md)
- [Harness adapters](references/harness-adapters.md)
- [Platform adapters](references/platform-adapters.md)
- [Skills](references/skills.md)
- [Failure modes](references/failure-modes.md)
- [Observability](references/observability.md)

## Scripts

- `scripts/check_workspace.py <path>`: required files, stage contracts, and relative links.
- `scripts/check_contracts.py`: validates the example skill and adapter manifests.

Both are standard-library Python 3. Copy them into `_tools/` if the workspace needs them.

## What not to do

- Do not put content in `AGENTS.md`.
- Do not create a stage with no output or no check.
- Do not claim a harness is vendor-neutral without an adapter contract.
- Do not copy a complete client folder into a public workspace.
- Do not let a model be the only judge of its own output.
