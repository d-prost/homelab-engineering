# Rollback needs re-verification

Copying the previous files back is not enough to call a rollback successful.

The previous configuration still has to be applied and checked again.

A useful rollback result therefore looks like:

```text
candidate failed
      |
      v
previous managed state restored
      |
      v
previous runtime reapplied
      |
      v
previous functional checks pass
```

Only the final step tells me that rollback recovered the known application behavior.

This matters most when the failed candidate changed more than one managed file or when runtime state can survive a configuration restore.
