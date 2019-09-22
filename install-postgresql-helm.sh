kubectl create -f postgresql-pv.yaml
helm install --name postgresql -f postgresql-values.yaml stable/postgresql
