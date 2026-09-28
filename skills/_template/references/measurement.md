# Measurement

> Annotated template. Every benchmark or example number is labeled illustrative unless it cites a verifiable source.

## Primary KPI

> The one number that says whether the program works. Define the numerator, the denominator, and the window.

- KPI: TODO (for example, placed-order rate per recipient within the flow window)
- Why this KPI: TODO

## Guardrail metrics

> Numbers that must not get worse while chasing the KPI. Say what movement should trigger a review.

| Guardrail | Why it matters | Review when |
|---|---|---|
| Unsubscribe rate | TODO | TODO (illustrative threshold) |
| Spam complaint rate | TODO | TODO (illustrative threshold) |
| Discount cost per order | TODO | TODO |

## Attribution

> Which attribution window and model to read, and the known bias. Flow-attributed revenue in any ESP tends to over-credit the flow because it counts orders that would have happened anyway. Say so, and say how to correct for it.

- Window: TODO
- Known bias: TODO

## Holdout guidance

> When a holdout is worth running, how to size it, and how long to run it. Explain the tradeoff between holdout size and the revenue given up during the test.

- When to hold out: TODO
- Sizing approach: TODO
- Duration: TODO
- Read-out: TODO (compare KPI between exposed and holdout groups, not flow-attributed revenue)
