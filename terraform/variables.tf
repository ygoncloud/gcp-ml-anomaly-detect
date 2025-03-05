variable "gcp_project" {
  description = "The GCP project ID"
  type        = string
}

variable "gcp_region" {
  description = "The region for GCP resources"
  type        = string
  default     = "us-central1"
}

variable "gke_cluster_name" {
  description = "The name of the GKE cluster"
  type        = string
  default     = "devops-cluster"
}

variable "ml_registry_name" {
  description = "Artifact Registry for ML model containers"
  type        = string
  default     = "ml-container-registry"
}

variable "log_bucket_name" {
  description = "Cloud Storage Bucket for Logs"
  type        = string
}
