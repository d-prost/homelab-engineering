# Backup is not recovery

A successful backup job proves that a backup operation completed. It does not prove that the result is sufficient to recover the application.

I treat these as separate states:

```text
backup exists
backup is readable
restore completes
application starts
representative behavior passes
```

Skipping the last steps is attractive because backup jobs are easy to automate and easy to graph. The failure usually appears only when the backup is needed.

For stateful changes, recent backup success is useful input. Functional restore evidence is stronger input. Neither should be inferred from the other.
