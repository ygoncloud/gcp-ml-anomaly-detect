# Log Anomaly Detection

[![CI/CD](https://github.com/mumei/gcp-ml-anomaly-detect/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/mumei/gcp-ml-anomaly-detect/actions/workflows/ci-cd.yml)

This project provides a framework for detecting anomalies in application logs using machine learning. It is designed to be deployed on Google Cloud Platform (GCP) using Kubernetes (GKE) and includes a complete CI/CD pipeline using GitHub Actions.

The system collects logs from Kubernetes pods, uses a trained machine learning model to detect anomalies, and provides tools for monitoring and alerting.

## Features

*   **Machine Learning-Based Anomaly Detection:** A pre-trained LSTM model for identifying anomalous log entries.
*   **GCP Deployment:** All infrastructure is provisioned using Terraform, and the application is deployed to GKE.
*   **CI/CD Pipeline:** A complete GitHub Actions workflow for continuous integration and deployment.
*   **Monitoring and Alerting:** Integration with Prometheus, Grafana, and the ELK stack for observability.
*   **Structured Logging:** The application uses structured logging in JSON format for easy parsing and analysis.

## Getting Started

### Prerequisites

*   [Terraform](https://www.terraform.io/)
*   [Google Cloud SDK](https://cloud.google.com/sdk)
*   [Docker](https://www.docker.com/)
*   [kubectl](https://kubernetes.io/docs/tasks/tools/)
*   [Python 3.9+](https://www.python.org/)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/mumei/gcp-ml-anomaly-detect.git
    cd gcp-ml-anomaly-detect
    ```

2.  **Set up your GCP project:**

    ```bash
    gcloud auth application-default login
    gcloud config set project <YOUR_PROJECT_ID>
    ```

3.  **Deploy the infrastructure:**

    ```bash
    terraform init
    terraform apply
    ```

4.  **Deploy the application:**

    The CI/CD pipeline will automatically deploy the application when you push to the `main` branch. Alternatively, you can run the deployment script manually:

    ```bash
    ./scripts/deploy.sh
    ```

## Monitoring

Once the application is deployed, you can access the monitoring dashboards:

*   **Grafana:** `kubectl port-forward svc/grafana 3000:80 -n monitoring`
*   **Kibana:** `kubectl port-forward svc/kibana 5601:80 -n monitoring`

## Cleanup

To remove all resources created by this project, run:

```bash
terraform destroy
```