# Authority model

Several tools can describe the same system without all of them becoming authorities.

The model I use is:

```text
Git       = desired state
Monitoring = runtime observation
Scripts   = bounded mechanisms
Human     = Production authority
Evidence  = dated proof
```

The distinctions matter.

A healthy monitoring check does not mean a proposed configuration is correct. A merged commit does not mean Production accepted it. A successful backup job does not prove that the data can be restored. A dated proof does not stay current forever.

Keeping those responsibilities separate avoids a common failure mode in small environments: a convenient dashboard slowly becomes the place that edits configuration, decides health, starts deployments and stores history at the same time.

The operational system can still be simple. The separation is conceptual first.
