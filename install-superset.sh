##wget https://raw.githubusercontent.com/helm/charts/master/stable/superset/values.yaml
#wget https://raw.githubusercontent.com/phenom1711/superset/master/superset-value.yaml
#kubectl create configmap superset-config --from-file superset_config.py 
helm install --name superset -f superset-value.yaml stable/superset
