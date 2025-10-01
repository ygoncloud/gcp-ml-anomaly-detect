terraform {
  backend "gcs" {
    bucket = "your-terraform-state-bucket"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = var.gcp_project
  region  = var.gcp_region
}

# Enable required GCP services
resource "google_project_service" "enable_services" {
  for_each = toset([
    "container.googleapis.com",
    "artifactregistry.googleapis.com",
    "cloudresourcemanager.googleapis.com"
  ])
  project = var.gcp_project
  service = each.key
}

# Create GKE Cluster
resource "google_container_cluster" "gke_cluster" {
  name     = var.gke_cluster_name
  location = var.gcp_region
  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "primary-node-pool"
  cluster    = google_container_cluster.gke_cluster.name
  node_count = 2

  node_config {
    machine_type = "e2-medium"
    oauth_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

# Create Artifact Registry for ML Model Container Images
resource "google_artifact_registry_repository" "ml_registry" {
  provider = google
  project  = var.gcp_project
  location = var.gcp_region
  repository_id = "ml-container-registry"
  format = "DOCKER"
}

# Create Cloud Storage Bucket for Logs
resource "google_storage_bucket" "log_bucket" {
  name          = "${var.gcp_project}-log-bucket"
  location      = var.gcp_region
  force_destroy = true
}
