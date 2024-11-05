# How to install

1. Create `monitoring` namespace.

2. Install `prometheus-operator-crds`

    [How to install](../prometheus-operator-crds/README.md)

3. Add files to `custom-resources`:

    ```yaml
    clusters/<CLUSTER>/custom-resources/monitoring/prometheus/helm-release.yaml

    ---
    apiVersion: helm.toolkit.fluxcd.io/v2beta1
    kind: HelmRelease
    metadata:
      name: prometheus
      namespace: flux-system
    spec:
      releaseName: prometheus
      chart:
        spec:
          version: 65.x
      values:
    ```

    [Chart values](https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/values.yaml)

    ```yaml
    clusters/<CLUSTER>/custom-resources/monitoring/prometheus/kustomization.yaml

    ---
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    resources:
      - ../../../../../components/apps/prometheus
    patches:
      - path: helm-release.yaml
        target:
          kind: HelmRelease
    ```

4. Connect to `sync-code`:

    ```yaml
    clusters/<CLUSTER>/sync-code/monitoring/prometheus.yaml

    ---
    apiVersion: kustomize.toolkit.fluxcd.io/v1
    kind: Kustomization
    metadata:
      name: prometheus
      namespace: flux-system
    spec:
      interval: 10m0s
      dependsOn:
        - name: repos
      sourceRef:
        kind: GitRepository
        name: flux-system
      path: ./clusters/<CLUSTER>/custom-resources/monitoring/prometheus
      prune: true
      wait: true
      timeout: 5m0s
      postBuild:
        substituteFrom:
          - kind: ConfigMap
            name: cluster-variables
            # Use this ConfigMap if it exists, but proceed if it doesn't.
            optional: false
    ```

## Additional info
