# Desired state is not accepted state

Git is good at answering:

> what configuration do I intend to run?

It is not good at answering:

> did this exact change become healthy in the target environment?

Those are different facts.

A commit becomes a deployment candidate. Acceptance happens only after the real target has passed the checks that matter for that service and the result has been recorded durably.

This distinction became useful enough to extract into [DeployInvariant](https://github.com/d-prost/deploy-invariant), but it applies more broadly than deployment tooling.

Historical acceptance is also not current health. Runtime observation still has its own job.
