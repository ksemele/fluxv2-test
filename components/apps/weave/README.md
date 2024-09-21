# How to install

We create an `admin` user with a random password because without it, Weave will not run.

[Chart values](https://github.com/weaveworks/weave-gitops/blob/main/charts/gitops-server/values.yaml)

1. Connect to `sync-code`:

    ```yaml
    clusters/<CLUSTER>/sync-code/flux-system/weave.yaml

    ---
    apiVersion: kustomize.toolkit.fluxcd.io/v1
    kind: Kustomization
    metadata:
      name: weave-gitops
      namespace: flux-system
    spec:
      dependsOn:
        - name: repos
      interval: 5m
      retryInterval: 1m
      timeout: 15m
      sourceRef:
        kind: GitRepository
        name: flux-system
      path: ./components/apps/weave
      prune: true
      wait: true
    ```

## Additional info
