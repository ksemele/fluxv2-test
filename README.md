# Flux monorepo demo repository

# WIP

This is a repository with an example of organizing a monorepo for multiple clusters using [Flux]() tool.

The first version is described in the article [here]() and the repository for it is located [here]()

This is a new version that I want to update constantly.

## Prerequisites

1. Create your Kubernetes cluster (my simple example available [here]())
2. Clone this repo
3. Bootstrap flux v2:
```shell
kubectl apply -f ./components/flux/prod/gotk-components.yaml
```
4. Apply flux resource to sync this repo and your cluster
```
kubectl apply -f clusters/cluster-002/sync-code/flux-system/gotk-sync.yaml
```

5. Check Weave gitops
forward port
```
kubectl -n flux-system port-forward svc/weave-gitops 9001:9001
```
login on http://localhost:9001

use `admin:admin`

6. Uninstall flux
```
flux uninstall
```
