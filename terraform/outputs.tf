```hcl
output "gke_cluster_endpoint" {
  description = "The endpoint of the GKE cluster"
  value       = google_container_cluster.gke_cluster.endpoint
}

output "ml_registry_url" {
  description = "URL of the Artifact Registry for ML container images"
  value       = google_artifact_registry_repository.ml_registry.id
}

output "log_bucket_name" {
  description = "The name of the Cloud Storage Bucket for logs"
  value       = google_storage_bucket.log_bucket.name
}
```
