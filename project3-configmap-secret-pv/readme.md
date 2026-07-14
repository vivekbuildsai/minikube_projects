# 🚀 Project 3 - MySQL with Persistent Volumes, ConfigMaps & Secrets on Kubernetes

## 📌 Overview

This project demonstrates how to deploy a **stateful MySQL database** on Kubernetes using **Persistent Volumes (PV)**, **Persistent Volume Claims (PVC)**, **ConfigMaps**, and **Secrets**.

Unlike stateless applications, databases require persistent storage to ensure data is not lost when Pods are restarted or recreated.

This project focuses on implementing production-style Kubernetes configuration management and storage concepts.

---

# 🏗 Architecture

```text
                        MySQL Deployment
                               │
                               ▼
                          MySQL Pod
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
     ConfigMap             Secret              Volume Mount
          │                    │                    │
          ▼                    ▼                    ▼
 MYSQL_DATABASE      MYSQL_ROOT_PASSWORD        mysql-pvc
                                                    │
                                                    ▼
                                               Persistent Volume
                                                    │
                                                    ▼
                                              Local Storage
```

---

# 📂 Project Structure

```text
project3-configmap-secret-pv/

├── k8s/
│   ├── persistent-volume.yaml
│   ├── persistent-volume-claim.yaml
│   ├── mysql-configmap.yaml
│   ├── mysql-secret.yaml
│   ├── mysql-deployment.yaml
│   └── mysql-service.yaml
│
└── README.md
```

---

# ⚙ Technologies Used

- Kubernetes
- Minikube
- Docker
- MySQL 8.0
- YAML
- kubectl

---

# 🚀 Features

- Deploy MySQL on Kubernetes
- Persistent Storage using Persistent Volume
- Persistent Volume Claim
- ConfigMap for non-sensitive configuration
- Secret for sensitive credentials
- Environment Variable Injection
- MySQL ClusterIP Service
- Data Persistence across Pod recreation

---

# 📦 Kubernetes Resources

| Resource | Purpose |
|----------|---------|
| PersistentVolume | Provides persistent storage |
| PersistentVolumeClaim | Requests storage for Pods |
| Deployment | Manages MySQL Pod |
| Service | Internal ClusterIP access |
| ConfigMap | Stores database configuration |
| Secret | Stores database password |

---

# 🌐 Architecture Flow

```text
Application
      │
      ▼
MySQL Service (ClusterIP)
      │
      ▼
MySQL Pod
      │
      ▼
Environment Variables
      │
      ├───────────────┐
      ▼               ▼
 ConfigMap         Secret
      │               │
      └──────┬────────┘
             ▼
      Volume Mount
             │
             ▼
Persistent Volume Claim
             │
             ▼
 Persistent Volume
             │
             ▼
 Local Storage
```

---

# 📁 Persistent Storage Workflow

```text
Pod

↓

Persistent Volume Claim

↓

Persistent Volume

↓

Physical Storage
```

The Pod never communicates directly with the Persistent Volume. Kubernetes binds the Persistent Volume Claim to an available Persistent Volume.

---

# 🔐 ConfigMap

Used to store non-sensitive configuration.

Example:

```yaml
data:
  MYSQL_DATABASE: employee_db
  MYSQL_HOST: mysql-service
```

---

# 🔒 Secret

Used to store sensitive information.

Example:

```yaml
data:
  MYSQL_ROOT_PASSWORD: cm9vdDEyMw==
```

The password is Base64 encoded before being stored in Kubernetes.

---

# ▶ Running the Project

## Start Minikube

```bash
minikube start
```

---

## Deploy Persistent Volume

```bash
kubectl apply -f k8s/persistent-volume.yaml
```

---

## Deploy Persistent Volume Claim

```bash
kubectl apply -f k8s/persistent-volume-claim.yaml
```

---

## Deploy ConfigMap

```bash
kubectl apply -f k8s/mysql-configmap.yaml
```

---

## Deploy Secret

```bash
kubectl apply -f k8s/mysql-secret.yaml
```

---

## Deploy MySQL

```bash
kubectl apply -f k8s/mysql-deployment.yaml
```

---

## Deploy Service

```bash
kubectl apply -f k8s/mysql-service.yaml
```

---

# 🔍 Verify Resources

```bash
kubectl get pv

kubectl get pvc

kubectl get deployments

kubectl get pods

kubectl get svc

kubectl get configmap

kubectl get secrets
```

---

# 🧪 Verify Data Persistence

Connect to MySQL

```bash
kubectl exec -it <mysql-pod-name> -- mysql -u root -p
```

Select the database

```sql
USE employee_db;
```

Create a table

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

Insert data

```sql
INSERT INTO employees VALUES
(1,'Vivek'),
(2,'John');
```

Verify

```sql
SELECT * FROM employees;
```

Delete the MySQL Pod

```bash
kubectl delete pod <mysql-pod-name>
```

Wait for Kubernetes to create a new Pod.

Reconnect to MySQL

```bash
kubectl exec -it <new-mysql-pod-name> -- mysql -u root -p
```

Verify the data

```sql
USE employee_db;

SELECT * FROM employees;
```

If the records still exist, the Persistent Volume is working correctly.

---

# 🔍 Useful Commands

```bash
kubectl get pv

kubectl get pvc

kubectl get pods

kubectl get deployments

kubectl get svc

kubectl get configmap

kubectl get secrets

kubectl describe pvc mysql-pvc

kubectl describe pv mysql-pv

kubectl logs <pod-name>

kubectl exec -it <pod-name> -- bash

kubectl delete pod <pod-name>
```

---

# 📚 Kubernetes Concepts Learned

- Persistent Volume (PV)
- Persistent Volume Claim (PVC)
- Static Provisioning
- Storage Binding
- hostPath Volumes
- Volume Mounts
- ConfigMaps
- Secrets
- Base64 Encoding
- Environment Variables
- MySQL Deployment
- ClusterIP Service
- Stateful Application Storage

---

# 🎯 Learning Outcomes

After completing this project, I gained practical experience with:

- Deploying a stateful application on Kubernetes
- Configuring persistent storage using PV and PVC
- Managing application configuration with ConfigMaps
- Managing sensitive credentials with Secrets
- Injecting environment variables into containers
- Persisting MySQL data across Pod recreation
- Understanding static vs dynamic storage provisioning
- Troubleshooting Kubernetes storage resources

---

# 🧠 Key Interview Topics Covered

- ConfigMap vs Secret
- Persistent Volume vs Persistent Volume Claim
- Static vs Dynamic Provisioning
- hostPath Volumes
- Volume Mounts
- Environment Variable Injection
- ClusterIP Services
- Stateful vs Stateless Applications
- Kubernetes Storage Lifecycle

---

# 📌 Future Improvements

- Replace Deployment with StatefulSet
- Use Headless Service
- Dynamic Provisioning with StorageClass
- Use MySQL Replication
- Deploy using Helm
- Store secrets in HashiCorp Vault
- Add automated backups
- Deploy on a cloud Kubernetes cluster (EKS, AKS, or GKE)
