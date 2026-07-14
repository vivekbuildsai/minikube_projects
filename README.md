# 🚀 Project 1 - Deploy Nginx on Kubernetes using Minikube

## 📌 Overview

This project demonstrates the deployment of a simple **Nginx web server** on a **Kubernetes cluster using Minikube**.

The primary goal of this project is to understand the core Kubernetes objects and deployment workflow by containerizing and exposing an application.

This is the first project in my Kubernetes learning journey.

---

# 🏗 Architecture

```
           Browser
               │
               ▼
     NodePort Service
               │
               ▼
          Nginx Pod
               │
               ▼
         Nginx Container
```

---

# 📂 Project Structure

```
project1-nginx/

├── nginx-deployment.yaml
├── nginx-service.yaml
└── README.md
```

---

# ⚙ Technologies Used

- Kubernetes
- Minikube
- Docker
- Nginx
- kubectl
- YAML

---

# 🚀 Features

- Deploy Nginx using a Kubernetes Deployment
- Expose the application using a NodePort Service
- Access the application from a web browser
- Learn Kubernetes resource management using kubectl
- Understand Pod lifecycle and Service networking

---

# 📦 Kubernetes Resources

## Deployment

- 1 Replica
- Nginx Container
- Automatic Pod recreation on failure

## Service

- NodePort
- External browser access

---

# 🌐 Architecture Flow

```
Browser
    │
    ▼
NodePort Service
    │
    ▼
Nginx Pod
    │
    ▼
Nginx Container
```

---

# ▶ Running the Project

## Clone Repository

```bash
git clone <repository-url>
cd project1-nginx
```

---

## Start Minikube

```bash
minikube start
```

---

## Apply Kubernetes Manifests

Deploy Nginx

```bash
kubectl apply -f nginx-deployment.yaml
```

Create the Service

```bash
kubectl apply -f nginx-service.yaml
```

---

## Verify Deployment

```bash
kubectl get deployments
```

---

## Verify Pods

```bash
kubectl get pods
```

---

## Verify Services

```bash
kubectl get svc
```

---

## Access the Application

```bash
minikube service nginx-service
```

This command automatically opens the Nginx welcome page in your default web browser.

---

# 🔍 Useful Commands

```bash
kubectl get pods

kubectl get deployments

kubectl get svc

kubectl describe pod <pod-name>

kubectl logs <pod-name>

kubectl exec -it <pod-name> -- sh

kubectl delete pod <pod-name>

kubectl rollout restart deployment nginx-deployment

kubectl rollout status deployment nginx-deployment

kubectl get all
```

---

# 📚 Kubernetes Concepts Learned

- Kubernetes Cluster
- Minikube
- Pods
- Deployments
- ReplicaSets
- Services
- NodePort
- Labels
- Selectors
- YAML Manifests
- kubectl Commands
- Pod Lifecycle
- Container Networking

---

# 🧠 Key Learnings

During this project, I learned:

- How Kubernetes Deployments manage Pods
- Difference between Pods and Deployments
- How ReplicaSets maintain the desired number of Pods
- How NodePort exposes an application outside the cluster
- How Services route traffic to Pods using Labels and Selectors
- How to inspect Kubernetes resources using kubectl
- Basic troubleshooting using logs and describe commands

---

# 🎯 Skills Demonstrated

- Kubernetes Fundamentals
- Container Orchestration
- YAML Configuration
- kubectl CLI
- Kubernetes Networking
- Application Deployment
- Service Exposure
- Troubleshooting Kubernetes Resources

---

# 📌 Future Improvements

The next projects in this learning series will cover:

- Multi-tier applications
- ClusterIP Services
- ConfigMaps
- Secrets
- Persistent Volumes
- Ingress
- Horizontal Pod Autoscaler (HPA)
- Helm Charts
- Monitoring with Prometheus & Grafana
- CI/CD with GitHub Actions
