#!/bin/bash

PROJECT_ID="your-gcp-project-id"
REGION="us-central1"
CLUSTER_NAME="devops-cluster"

# Authenticate with GCP
gcloud auth configure-docker

echo "🔹 Building and Pushing the Log Anomaly Detection Service..."
# Build and push the ML Log Anomaly Detection Service
docker build -t gcr.io/$PROJECT_ID/log-anomaly-service ./ml
docker push gcr.io/$PROJECT_ID/log-anomaly-service

# Deploy the ML Log Anomaly Detection Service
kubectl apply -f k8s/log-anomaly-deployment.yaml
kubectl apply -f k8s/log-anomaly-service.yaml

echo "🔹 Deploying to Kubernetes..."
gcloud container clusters get-credentials $CLUSTER_NAME --region $REGION

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml

kubectl apply -f monitoring/logstash-config.yaml
kubectl apply -f monitoring/kibana-alerts.json
kubectl apply -f monitoring/prometheus-values.yaml
kubectl apply -f monitoring/grafana-dashboards.yaml

# Deploy OpenTelemetry Collector
kubectl apply -f monitoring/otel-config.yaml

echo "✅ Deployment completed!"

echo "🔹 Retrieving External Services..."
kubectl get services -n monitoring
kubectl get ingress
