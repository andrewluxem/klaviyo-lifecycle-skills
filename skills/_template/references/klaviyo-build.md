# Klaviyo build notes

> Annotated template. Describe the build at the level of program design.
>
> Ground rule: for tool names, arguments, and API shapes, defer to `klaviyo-labs/agent-context` and the live Klaviyo API or MCP catalog. Never trust this file over the live catalog. Do not paste API payloads here.

## Trigger

> Which trigger type (list, segment, metric, price drop, date property) and which specific list, segment, or metric. Say why this trigger fits the program better than the alternatives.

- Trigger: TODO
- Why: TODO

## Filters

> Profile filters decide who can enter. Flow filters are rechecked before every step. Name each filter and the failure it prevents.

| Filter | Type (profile or flow) | Condition | Prevents |
|---|---|---|---|
| TODO | Flow | TODO (for example, placed order zero times since starting this flow) | TODO |

## Conditional splits

> One row per split. Say what each branch receives and why.

| Split | Condition | Yes branch | No branch | Why |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

## Required data

> Event properties, profile properties, and catalog fields the templates and splits depend on. For each, name what breaks when it is missing and the fallback.

| Field | Source (event, profile, catalog) | Used by | Fallback if missing |
|---|---|---|---|
| TODO | TODO | TODO | TODO |
