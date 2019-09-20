##wget https://raw.githubusercontent.com/helm/charts/master/stable/superset/values.yaml
helm install --name superset -f superset-values.yaml stable/superset
