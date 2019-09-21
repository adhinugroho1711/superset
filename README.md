# superset

## how to install
```
1. install postgresql
2. install redis
3. install superset
```

##  check postgres
```
$ kubectl get svc postgres
NAME       TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
postgres   NodePort   10.107.71.253   <none>        5432:31070/TCP   5m
```

## login postgresql
```
psql -h localhost -U postgresadmin --password -p 31070 postgresdb
```
