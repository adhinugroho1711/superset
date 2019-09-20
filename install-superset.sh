##wget https://raw.githubusercontent.com/helm/charts/master/stable/superset/values.yaml
snap install helm --classic
kubectl -n kube-system create serviceaccount tiller
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller --upgrade

sleep 2m

#wget https://raw.githubusercontent.com/phenom1711/superset/master/superset-value.yaml
helm install --name superset -f superset-value.yaml stable/superset
