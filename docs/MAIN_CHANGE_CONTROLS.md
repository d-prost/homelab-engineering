# Main change controls

The repository uses a small change-control boundary for `main`.

The intended rules are stored in [`.github/rulesets/main.json`](../.github/rulesets/main.json):

- changes arrive through pull requests;
- zero human approvals are required for the single-maintainer model;
- the `Public boundary` check must pass against the latest base state;
- force-push and branch deletion are blocked;
- squash is the only merge method.

The policy protects the public repository boundary. It does not turn this repository into an operational authority for the HomeLab.

Applying the policy requires repository Administration permission:

```bash
gh api \
  --method POST \
  -H 'Accept: application/vnd.github+json' \
  -H 'X-GitHub-Api-Version: 2022-11-28' \
  repos/d-prost/homelab-engineering/rulesets \
  --input .github/rulesets/main.json
```

If a ruleset with the same name already exists, update that ruleset instead of creating a duplicate.
