# Readme

Welcome to app templates!

## How to use app templates

Read `README.md` for each app. It must contain the minimum configurations to deploy the app.

## How to add app template

1. create `components/apps/<APP_NAME>`
2. create `helm-release.yaml` with default values

(e.g. Prometheus `kube-state-metrics` config for flux)
other files if needed and Kustomization from `kustomize.config.k8s.io/v1beta1` with list of files.

3. create `README.md` (! linter is active for md files. more info about format: [markdownlint rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#rules))

`README.md` [template](../../examples/template-README.md)

4. If app use new repo - add it to `components/apps/repos`

## Additional info
