#!/bin/bash

PROJECT_ID="your-gcp-project-id"
REGION="us-central1"
CLUSTER_NAME="devops-cluster"

echo "🔹 Deleting Kubernetes Resources..."
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml
kubectl delete -f k8s/ingress.yaml

kubectl delete -f monitoring/logstash-config.yaml
kubectl delete -f monitoring/kibana-alerts.json
kubectl delete -f monitoring/prometheus-values.yaml
kubectl delete -f monitoring/grafana-dashboards.yaml

kubectl delete -f monitoring/otel-config.yaml

echo "🔹 Destroying GKE Cluster..."
gcloud container clusters delete $CLUSTER_NAME --region $REGION --quiet

echo "🔹 Cleaning up orphaned resources..."
gcloud compute firewall-rules delete allow-gke -q
gcloud compute networks subnets delete gke-subnet -q
gcloud compute networks delete gke-network -q
gcloud container images delete gcr.io/$PROJECT_ID/log-anomaly-service --force-delete-tags -q

echo "✅ Cleanup completed!"
