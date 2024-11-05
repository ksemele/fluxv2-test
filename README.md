# Flux monorepo demo repository

This is a repository with an example of organizing a monorepo for multiple clusters using [FluxCD](https://github.com/fluxcd/flux2) tool.

The first version is described in the article [here](https://medium.com/@ksemele/flux-v2-monorepo-experience-2973cd501fdd) and the repository for it is located [here](https://github.com/ksemele/flux-monorepo)

This is a new version that I want to update constantly.

## Prerequisites

1. Create your Kubernetes cluster (my simple example for GKE available [here](https://github.com/ksemele/tf-gke-test), kind or minikube will work too)
2. Clone this repo
3. Bootstrap flux v2:

```shell
kubectl apply -f ./components/flux/prod/gotk-components.yaml
```

4. Apply flux resource to sync this repo and your cluster

```shell
kubectl apply -f clusters/cluster-002/sync-code/flux-system/gotk-sync.yaml
```

5. Check Weave gitops

forward port

```shell
kubectl -n flux-system port-forward svc/weave-gitops 9001:9001
```

login on `http://localhost:9001`

use `admin:admin`

6. Uninstall flux

```shell
flux uninstall
```
