##wget https://raw.githubusercontent.com/helm/charts/master/stable/superset/values.yaml
wget https://raw.githubusercontent.com/phenom1711/superset/master/superset-value.yaml
helm install --name superset -f superset-values.yaml stable/superset
