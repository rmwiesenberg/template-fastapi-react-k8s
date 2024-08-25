#!/bin/bash

kubectl create serviceaccount template-serviceaccount

kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: template-secret
  annotations:
    kubernetes.io/service-account.name: template-serviceaccount
type: kubernetes.io/service-account-token
EOF

kubectl get secret template-secret -n default -o yaml
