# How to apply

1. Create your Kubernetes cluster
2. Clone this repo
3. Bootstrap flux v2

Here is one of possible ways to simple bootstrap:

install flux cli:

If you creating your own repo (this file contain all CRD's for flux controllers and resources, already exist in this repo):
```
flux install --export > clusters/ksemele-demo-gke/sync-code/flux-system/gotk-components.yaml
```

Check your cluster is ready to install flux:
```
flux check --pre
```
e.g.
```
$ flux check --pre
► checking prerequisites
✔ Kubernetes 1.25.7-gke.1000 >=1.20.6-0
✔ prerequisites checks passed
```

Install flux into your cluster (check your context):
```
flux install
```

Optional: check installation after complete
```
flux check
```

4. apply flux resource to sync this repo and your cluster
```
kubectl apply -f clusters/ksemele-demo-gke/sync-code/flux-system/gotk-sync.yaml
```
