# How to install

[Chart values](https://github.com/bitnami/charts/blob/main/bitnami/nginx/values.yaml)

1. Add files to your `custom-resources`

```yaml
# helm-release.yaml
---
apiVersion: helm.toolkit.fluxcd.io/v2beta1
kind: HelmRelease
metadata:
  name: nginx
  namespace: <NAMESPACE>
spec:
  targetNamespace: <NAMESPACE>
  storageNamespace: <NAMESPACE>
  chart:
    spec:
      version: 18.2.3
#   values:
```

```yaml
# kustomization.yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../../../../components/apps/nginx
patches:
  - path: helm-release.yaml
    target:
      kind: HelmRelease
      name: nginx
```

1. Connect to `sync-code`:

```yaml
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: nginx-<POSTFIX>
  namespace: <NAMESPACE>
spec:
  patches:
  - patch: |

      - op: replace
        path: /metadata/name
        value: nginx-<POSTFIX>
      - op: replace
        path: /spec/releaseName
        value: nginx-<POSTFIX>
    target:
      kind: HelmRelease
      name: nginx
  interval: 5m
  retryInterval: 1m
  timeout: 15m
  sourceRef:
    kind: GitRepository
    name: flux-system
    namespace: flux-system
  path: ./clusters/<CLUSTER>/custom-resources/<NAMESPACE>/nginx-<POSTFIX>
  prune: true
  wait: true

```

## Additional info

### How to check availible versions

```shell
helm search repo bitnami/nginx --versions
```
