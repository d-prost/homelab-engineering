# Repository boundaries

The project is split by authority, not by how convenient it would be to keep files together.

## Private operations

The private operations repository owns the live environment:

- desired state;
- exact inventory and addressing;
- operational automation;
- backup and recovery implementation;
- current recovery evidence;
- runtime-specific configuration.

It is allowed to know the real system.

## HomeLab Engineering

This repository owns public engineering knowledge:

- decisions;
- experiments;
- incident lessons;
- recovery methods;
- comparisons;
- sanitized architecture.

It is not consumed by Production.

## DeployInvariant

[DeployInvariant](https://github.com/d-prost/deploy-invariant) owns the reusable deployment transaction mechanism that was general enough to separate from the HomeLab.

It does not own the HomeLab topology, monitoring stack, backup system or application catalog.

## Direction of travel

Information moves outward only after abstraction:

```text
private operation
      |
      +--> public engineering lesson
      |
      +--> reusable product mechanism
```

Neither public repository is a mirror of the private one.
