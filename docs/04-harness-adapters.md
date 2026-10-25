# Harness adapters

A harness adapter is the only place that knows which model provider is in use.

The core asks for a task. The adapter handles transport, tools, retries, usage, and provider errors.

## Interface

```text
HarnessAdapter
  id
  capabilities
  run(request) -> result

request
  task
  context_files
  tools
  budget

result
  output_path
  usage
  tool_calls
  errors
```

The exact language is yours. The boundary is not.

## Capabilities

Declare what the provider supports:

```json
{
  "tools": true,
  "streaming": false,
  "structured_output": true,
  "vision": false,
  "max_context": 200000
}
```

The core branches on capabilities, never on a provider name.

## What stays out of the adapter

- The argument and the voice
- The publish decision
- Platform rules
- Client data
- Guardrail policy

If a prompt contains the publication's positioning, it belongs in a skill or a prompt registry, not in the adapter.

## Prompts and skills

A skill owns the task contract. A prompt template is part of that skill, not part of the model adapter.

This lets the same skill run on two providers without copying the prompt into both.

## Budgets

The request carries a budget:

- maximum input tokens
- maximum output tokens
- maximum wall time
- maximum tool calls

The adapter enforces it and reports what was used. A provider that ignores the budget is a failed adapter.

## Fallback

A fallback chain is a composition decision:

```text
primary adapter
  -> secondary adapter
    -> human queue
```

The core asks for a result. It does not hardcode the chain. The composition root decides which adapters are available.

## Testing

Use a fake adapter in tests:

- returns a fixed path
- reports synthetic usage
- can simulate a timeout
- can simulate a malformed tool call

The entire core should run green with the fake adapter and no network access.
