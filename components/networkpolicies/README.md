# Namespace template

We use `common-template` for `NetworkPolicy` collection for any namespace.

For specific namespaces such as monitoring or kube-system add similar file to your `sync-code` directory:

```yaml
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: networkpolicies-<NAMESPACE>
  namespace: flux-system
spec:
  interval: 5m0s
  targetNamespace: <NAMESPACE>
  sourceRef:
    kind: GitRepository
    name: flux-system
  path: ./components/networkpolicies/namespace-templates/<NAMESPACE>
  prune: true
  wait: true
  timeout: 20m0s
  postBuild:
    substituteFrom:
      - kind: ConfigMap
        name: cluster-variables
        # Use this ConfigMap if it exists, but proceed if it doesn't.
        optional: false
```

All other namespaces should use `common-template` in their `custome-resources` directory.

## Variables convention

```yaml
KUBE_API_IP_CIDR
KUBE_SVC_IP_CIDR
KUBE_POD_IP_CIDR
KUBE_MASTER_IP_CIDR
KUBE_WORKER_IP_CIDR
PRIVATE_IP_CIDR
```

## How it works

[Official docs](https://fluxcd.io/flux/faq/#using-kustomize-variable-substitution)
