# Keep Production deployment explicit

## Decision

CI validates changes but does not automatically deploy the live HomeLab after a merge.

## Why

The environment is small and operated by one person. The value of automatic CD is therefore limited, while the cost of an unexpected stateful mutation can be high.

A merge means:

> this desired state passed repository review and validation.

It does not mean:

> mutate Production now.

The extra explicit step also gives recovery readiness and current runtime state a chance to influence the decision.

## What remains automated

Automation is still useful for deterministic checks:

- syntax and contract validation;
- secret scanning;
- disposable transaction proofs;
- dependency proposals;
- routine backups;
- monitoring.

The boundary is around Production mutation, not around automation in general.
