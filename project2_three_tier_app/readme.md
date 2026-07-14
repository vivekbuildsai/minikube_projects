# 🚀 Project 2 - Three-Tier Employee Application on Kubernetes (Minikube)

## 📌 Overview

This project demonstrates how to deploy a **three-tier application** on **Kubernetes using Minikube**.

The application consists of:

* **Frontend** – Nginx serving a static web page
* **Backend** – Flask REST API
* **Kubernetes** – Deployments and Services for each component

The project focuses on understanding Kubernetes networking, Deployments, Services, Pod communication, and containerized applications.

---

# 🏗 Architecture

```text
                Browser
                    │
                    ▼
         Frontend Service (NodePort)
                    │
                    ▼
          Frontend Pod (Nginx)
                    │
                    ▼
      Backend Service (ClusterIP)
                    │
                    ▼
          Backend Pod (Flask API)
```

---

# 📂 Project Structure

```text
project2-three-tier-app/

├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── nginx.conf
│   └── Dockerfile
│
├── k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   └── frontend-service.yaml
│
└── README.md
```

---

# ⚙ Technologies Used

* Kubernetes
* Minikube
* Docker
* Python
* Flask
* Nginx
* HTML
* JavaScript
* YAML

---

# 🚀 Features

* Containerized Flask backend
* Containerized Nginx frontend
* Kubernetes Deployments
* ClusterIP Service
* NodePort Service
* Kubernetes DNS-based service discovery
* Reverse Proxy using Nginx
* REST API communication
* JSON data exchange

---

# 📦 Kubernetes Resources

## Backend

* Deployment
* ClusterIP Service

## Frontend

* Deployment
* NodePort Service

---

# 🌐 Networking Flow

```text
Browser
    │
    ▼
NodePort Service
    │
    ▼
Frontend Pod (Nginx)
    │
    ▼
Backend Service (ClusterIP)
    │
    ▼
Backend Pod (Flask)
```

---

# 📋 API Endpoint

### Get Employees

```http
GET /employees
```

### Sample Response

```json
[
  {
    "id": 1,
    "name": "John"
  },
  {
    "id": 2,
    "name": "Alice"
  },
  {
    "id": 3,
    "name": "David"
  }
]
```

---

# ▶ Running the Project

## Clone the Repository

```bash
git clone <repository-url>
cd project2-three-tier-app
```

---

## Start Minikube

```bash
minikube start
```

---

## Configure Docker to Use Minikube

```bash
eval $(minikube docker-env)
```

---

## Build Backend Image

```bash
cd backend
docker build -t employee-backend:v1 .
```

---

## Build Frontend Image

```bash
cd ../frontend
docker build -t employee-frontend:v1 .
```

---

## Deploy Backend

```bash
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
```

---

## Deploy Frontend

```bash
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
```

---

## Verify Resources

```bash
kubectl get deployments

kubectl get pods

kubectl get svc
```

---

## Access the Application

```bash
minikube service frontend-service
```

---

# 🔍 Useful Kubernetes Commands

```bash
kubectl get pods

kubectl get deployments

kubectl get svc

kubectl describe pod <pod-name>

kubectl logs <pod-name>

kubectl exec -it <pod-name> -- sh

kubectl rollout restart deployment backend-deployment

kubectl get endpoints
```

---

# 📚 Kubernetes Concepts Learned

* Pods
* Deployments
* ReplicaSets
* Services
* NodePort
* ClusterIP
* Labels
* Selectors
* Docker Images
* Kubernetes DNS
* Reverse Proxy
* Pod-to-Pod Communication
* YAML Manifests
* Container Networking

---

# 🎯 Learning Outcomes

After completing this project, I gained hands-on experience with:

* Deploying containerized applications on Kubernetes
* Building Docker images for frontend and backend services
* Creating Kubernetes Deployments and Services
* Implementing service-to-service communication using ClusterIP
* Exposing applications externally using NodePort
* Configuring Nginx as a reverse proxy
* Understanding Kubernetes DNS and service discovery
* Debugging applications using kubectl commands

---

# 📌 Future Improvements

* Integrate MySQL database
* Use ConfigMaps
* Use Secrets
* Add Persistent Volumes
* Implement Ingress
* Add Horizontal Pod Autoscaler
* Create Helm Charts
* Add CI/CD using GitHub Actions

