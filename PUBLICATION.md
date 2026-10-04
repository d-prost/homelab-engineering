# Publication boundary

This repository is written from real operational work, but it is not a sanitized clone of the private operations repository.

The preferred path is:

```text
understand -> abstract -> rewrite -> review -> publish
```

Copying a private file and deleting obvious secrets is not enough.

## Never publish

Keep the following outside this repository:

- exact live inventory and current placement;
- private addresses and internal DNS names;
- usernames, credentials, private keys and tokens;
- firewall rules that describe the live perimeter in detail;
- backup paths, repository identifiers and snapshot identifiers;
- break-glass procedures and authentication topology;
- live recovery receipts or exact recovery artifact locations;
- unresolved vulnerabilities in the running environment;
- personal data or application data.

## Safe abstraction

Prefer roles over identities:

```text
always-on infrastructure host
secondary infrastructure host
workload host
offsite backup destination
```

Prefer the reason for a decision over a complete inventory of what currently runs where.

Prefer representative or synthetic examples over copied operational output.

## Evidence

Public writing can describe what counts as evidence and how a proof was designed. The private evidence itself stays private unless it was created specifically as a public-safe, synthetic example.

Dated observations are not permanent truth. A document must not imply that a historical check proves the current runtime state.
