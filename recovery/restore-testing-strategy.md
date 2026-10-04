# Restore testing strategy

A backup is useful only when the recovery path is known well enough to trust.

The restore test I prefer has five parts:

1. select the exact recovery generation;
2. restore into an isolated target;
3. start the application with compatible configuration and images;
4. verify representative application behavior or data;
5. remove the disposable recovery environment.

Container health by itself is usually too weak. A database can start with the wrong data. A media service can answer HTTP while representative content is missing. A document system can be healthy while its index or attachments are incomplete.

## Generation sensitivity

Recovery evidence belongs to the state it proved.

A later change can invalidate an earlier restore proof when it changes:

- data format or schema;
- persistent paths;
- application version compatibility;
- backup method;
- encryption or secret requirements;
- restore procedure.

This is why recovery readiness is tracked separately from service health.

## What not to claim

A successful restore test does not prove every disaster scenario. The useful result is narrower:

> this generation was restored under these conditions and passed these checks.

That is enough to make recovery decisions better without pretending the proof is permanent.
