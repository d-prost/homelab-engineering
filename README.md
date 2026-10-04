# HomeLab Engineering

A public engineering record from a real self-hosted environment.

I use this repository for the parts of my HomeLab work that remain useful after the live details are removed: architecture decisions, experiments, incident lessons, recovery work and comparisons. It is not the operational source of truth for the environment.

[![Validate public boundary](https://github.com/d-prost/homelab-engineering/actions/workflows/validate.yml/badge.svg)](https://github.com/d-prost/homelab-engineering/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Repository boundary

The live HomeLab is managed elsewhere. This repository does not contain deployment inventory, internal addressing, private DNS, secrets, backup locations, live recovery artifacts or a complete current-service map.

Material reaches this repository only after it has been understood and generalized:

```text
real observation
      |
      v
understood cause or decision
      |
      v
generalized engineering point
      |
      v
public-safe write-up
```

Removing this repository must not change Production behavior.

## What belongs here

- architectural decisions that explain a useful trade-off;
- experiments with a clear question and result;
- sanitized incident notes with an understood cause;
- recovery methods and evidence models;
- comparisons where the decision matters more than the product list;
- lessons that have survived real operation.

A page that only repeats upstream documentation does not belong here.

## Layout

| Path | Purpose |
| --- | --- |
| `architecture/` | Sanitized system views and authority boundaries |
| `decisions/` | Design decisions and trade-offs |
| `experiments/` | Bounded experiments and their results |
| `incidents/` | Sanitized failure analysis and postmortems |
| `recovery/` | Backup, restore and recovery reasoning |
| `lessons/` | Reusable operational lessons |
| `comparisons/` | Decision-oriented tool and architecture comparisons |

The publication rules are in [`PUBLICATION.md`](PUBLICATION.md).

## Related work

[DeployInvariant](https://github.com/d-prost/deploy-invariant) is the reusable software project that grew out of one part of this work: guarded deployment transactions. It is intentionally separate from the broader HomeLab engineering record.

The actual HomeLab desired state and operational evidence remain in a private operations repository.

## Status

This repository starts small on purpose. I add material when there is a useful engineering result to preserve, not to mirror every service or every change in the lab.

## License

MIT. See [`LICENSE`](LICENSE).
