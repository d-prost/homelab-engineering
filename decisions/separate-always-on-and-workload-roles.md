# Separate always-on infrastructure from workload capacity

## Decision

Keep basic infrastructure responsibilities independent from the host that carries the heavier application state.

## Why

A workload host has different operating pressure:

- larger data sets;
- longer maintenance;
- more frequent application changes;
- higher power draw;
- more reasons to reboot or suspend.

DNS, ingress and monitoring have the opposite requirement: they should remain boring and available while application work is happening elsewhere.

Combining both roles makes routine application maintenance a network-infrastructure event.

## Trade-off

The separation costs another always-on node and a little more routing complexity.

For a small HomeLab, that cost is easier to reason about than making every application change share the same failure domain as name resolution and basic management.
