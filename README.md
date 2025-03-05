# 🚀 GCP DevOps: Machine Learning-Based Log Anomaly Detection

## 📌 Overview
This project automates **log anomaly detection** in a **GCP DevOps environment** using **machine learning, Kubernetes (GKE), ELK (Elasticsearch, Logstash, Kibana), Prometheus, Grafana, and OpenTelemetry**. The system **collects logs from Kubernetes pods, detects anomalies using an AI model, and triggers alerts for suspicious activity**.

---

## 🔧 Features
✅ **AI-Powered Log Anomaly Detection** with a trained ML model (TensorFlow/Keras)  
✅ **Log Collection & Analysis** using **ELK Stack (Elasticsearch, Logstash, Kibana)**  
✅ **Custom Dashboards** in **Grafana & Kibana**  
✅ **Distributed Tracing** with **OpenTelemetry**  
✅ **Alerts to Slack on Anomalies** via **Prometheus AlertManager**  
✅ **CI/CD Pipeline with Anomaly Detection Pre-Deployment Checks**  
✅ **Auto-Healing & Rollback on Bad Deployments**  

---

## 🏗️ Project Architecture
```
📂 gcp-devops-anomaly-detection
 ┣ 📂 k8s
 ┃ ┣ 📜 deployment.yaml           # Kubernetes Deployment & Service for app
 ┃ ┣ 📜 service.yaml              # Kubernetes Service
 ┃ ┣ 📜 ingress.yaml              # Ingress configuration for load balancing
 ┣ 📂 monitoring
 ┃ ┣ 📜 prometheus-values.yaml    # Prometheus custom configuration
 ┃ ┣ 📜 grafana-dashboards.yaml   # Pre-configured Grafana Dashboards
 ┃ ┣ 📜 logstash-config.yaml      # Logstash configuration for collecting logs
 ┃ ┣ 📜 kibana-alerts.json        # Kibana Alerts for log anomaly detection
 ┣ 📂 ml
 ┃ ┣ 📜 train_log_anomaly_model.py # Machine Learning script to train anomaly detection model
 ┃ ┣ 📜 log_anomaly_service.py     # API for real-time log anomaly detection
 ┃ ┣ 📜 log_sample.csv            # Sample log dataset for training ML model
 ┃ ┣ 📜 model/log_anomaly_model.h5 # Trained ML model
 ┣ 📂 scripts
 ┃ ┣ 📜 deploy.sh                 # Bash script to automate deployment
 ┃ ┣ 📜 cleanup.sh                # Bash script to clean up resources
 ┣ 📂 .github/workflows
 ┃ ┣ 📜 ci-cd.yml                 # GitHub Actions CI/CD pipeline with anomaly detection
 ┣ 📂 terraform
 ┃ ┣ 📜 main.tf                    # Terraform script to provision GCP infrastructure
 ┃ ┣ 📜 variables.tf               # Terraform variables for project setup
 ┃ ┣ 📜 outputs.tf                 # Terraform output values
 ┣ 📂 logs
 ┃ ┣ 📜 anomaly_detected.log        # Sample logs with anomalies
 ┃ ┣ 📜 normal_logs.log             # Sample logs without anomalies
 ┣ 📜 Dockerfile                    # Dockerfile to containerize the anomaly detection API
 ┣ 📜 app.py                         # Flask application for testing deployments
 ┣ 📜 requirements.txt               # Python dependencies
 ┣ 📜 README.md                      # Documentation for the project
```

---

## 📂 Setup & Deployment
### **1️⃣ Prerequisites**
Ensure you have installed:
- **Terraform** (>=1.0)
- **Google Cloud SDK (gcloud CLI)**
- **Docker**
- **kubectl**
- **Helm**
- **Python3, TensorFlow/Keras, Scikit-Learn**

### **2️⃣ Deploy GKE, ELK, and OpenTelemetry**
```bash
gcloud auth application-default login
gcloud config set project <YOUR_PROJECT_ID>
terraform init
terraform apply -auto-approve
```

### **3️⃣ Deploy Log Anomaly Detector**
```bash
python ml/log_anomaly_service.py
```

### **4️⃣ Run Deployment Script**
```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

### **5️⃣ Trigger CI/CD (Pushing Code)**
```bash
git add .
git commit -m "Deploy with log anomaly detection"
git push origin main
```

### **6️⃣ Access Monitoring Dashboards**
- **Grafana:** `kubectl port-forward svc/grafana 3000:80 -n monitoring`
- **Kibana:** `kubectl port-forward svc/kibana 5601:80 -n monitoring`
- **Prometheus:** `kubectl port-forward svc/prometheus-server 9090:80 -n monitoring`

---

## 📊 Observability & Monitoring
### **Grafana Dashboards**
- **Kubernetes Cluster Overview**
- **Anomaly Score Over Time**
- **CPU & Memory Usage per Pod**

### **Kibana Dashboards**
- **Log Anomaly Analysis**
- **Real-time Error Monitoring**
- **Security Log Insights**

### **OpenTelemetry Tracing**
- **Request Latency Visualization**
- **Distributed Tracing for API Calls**

---

## 📬 Alerts & Auto-Healing
🚨 **Slack Alerts on Log Anomalies** (via Prometheus AlertManager)  
🚨 **Auto-Rollback if Deployment Fails** (via GitHub Actions & Kubernetes)

```yaml
- name: Check for Anomalies Before Deployment
  run: |
    RESPONSE=$(curl -X POST -H "Content-Type: application/json" -d '{"log": "Test log for anomaly detection"}' http://log-anomaly-service:5000/detect_anomaly)
    IS_ANOMALOUS=$(echo $RESPONSE | jq '.is_anomalous')
    if [ "$IS_ANOMALOUS" = "true" ]; then
      echo "Anomaly detected! Aborting deployment."
      exit 1
    fi
```

---

## 🛑 Cleanup
```bash
terraform destroy -auto-approve
helm uninstall elasticsearch kibana logstash -n monitoring
```

---

## 📌 Why Use This?
✅ **AI-Powered Log Analysis** to detect security threats & system anomalies  
✅ **Custom Dashboards for Kubernetes, Logs & Traces**  
✅ **Auto-Rollback on Log Anomalies** before bad deployments occur  
✅ **Slack Alerts for Critical Errors** to DevOps teams  
✅ **Cloud-Native & CI/CD Ready** for scalable deployments  


