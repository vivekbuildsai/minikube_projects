# 🚀 Project 4 - MySQL StatefulSet with Headless Service on Kubernetes

## 📌 Overview

This project demonstrates how to deploy a **stateful MySQL database** on Kubernetes using **StatefulSets**, **Headless Services**, **Persistent Volume Claims (PVCs)**, **ConfigMaps**, and **Secrets**.

Unlike Deployments, StatefulSets provide:

- Stable Pod identities
- Stable network identities
- Dedicated storage for each Pod
- Ordered Pod creation and termination

This project simulates how production databases are deployed on Kubernetes.

---

# 🏗 Architecture

```text
                          Client
                             │
                             ▼
                    Headless Service
                   (clusterIP: None)
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
     mysql-0             mysql-1             mysql-2
        │                    │                    │
        ▼                    ▼                    ▼
   mysql-storage-0     mysql-storage-1     mysql-storage-2
        │                    │                    │
        ▼                    ▼                    ▼
 Persistent Volume     Persistent Volume    Persistent Volume
```

---

# 📂 Project Structure

```text
project4-statefulset-mysql/

├── k8s/
│   ├── mysql-headless-service.yaml
│   ├── mysql-statefulset.yaml
│   ├── mysql-configmap.yaml
│   ├── mysql-secret.yaml
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

- MySQL StatefulSet
- Headless Service
- Stable Pod Identity
- Stable DNS
- ConfigMap
- Secret
- Automatic PVC Creation
- volumeClaimTemplates
- Ordered Pod Creation
- Ordered Pod Termination
- Persistent Storage

---

# 📦 Kubernetes Resources

| Resource | Purpose |
|----------|---------|
| StatefulSet | Manages stateful MySQL Pods |
| Headless Service | Provides stable DNS identities |
| ConfigMap | Stores database configuration |
| Secret | Stores MySQL password |
| PVC | Dedicated storage for each Pod |
| PV | Persistent storage |

---

# 🌐 StatefulSet Architecture

```text
                   StatefulSet
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       mysql-0       mysql-1       mysql-2
          │              │              │
          ▼              ▼              ▼
      PVC-0          PVC-1          PVC-2
          │              │              │
          ▼              ▼              ▼
       PV-0           PV-1           PV-2
```

Each MySQL Pod owns its own Persistent Volume Claim.

---

# 🌐 Headless Service

Unlike a normal Kubernetes Service, a Headless Service does **not** create a ClusterIP.

```yaml
clusterIP: None
```

Instead, Kubernetes creates DNS records for each Pod.

Example:

```text
mysql-0.mysql

mysql-1.mysql

mysql-2.mysql
```

This allows applications to communicate with a specific Pod instead of being load balanced.

---

# 📁 volumeClaimTemplates

StatefulSets automatically create one Persistent Volume Claim for every Pod.

Example:

```text
mysql-0

↓

mysql-storage-mysql-0
```

```text
mysql-1

↓

mysql-storage-mysql-1
```

```text
mysql-2

↓

mysql-storage-mysql-2
```

No manual PVC creation is required.

---

# 🔐 ConfigMap

Stores non-sensitive configuration.

Example:

```yaml
data:
  MYSQL_DATABASE: employee_db
```

---

# 🔒 Secret

Stores sensitive configuration.

Example:

```yaml
data:
  MYSQL_ROOT_PASSWORD: cm9vdDEyMw==
```

The password is Base64 encoded before being stored.

---

# ▶ Running the Project

## Start Minikube

```bash
minikube start
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

## Deploy Headless Service

```bash
kubectl apply -f k8s/mysql-headless-service.yaml
```

---

## Deploy StatefulSet

```bash
kubectl apply -f k8s/mysql-statefulset.yaml
```

---

# 🔍 Verify Resources

```bash
kubectl get statefulsets

kubectl get pods

kubectl get pvc

kubectl get svc
```

Expected Pods

```text
mysql-0

mysql-1

mysql-2
```

Expected PVCs

```text
mysql-storage-mysql-0

mysql-storage-mysql-1

mysql-storage-mysql-2
```

---

# 📈 Scale the StatefulSet

Increase replicas.

```bash
kubectl scale statefulset mysql --replicas=3
```

Verify.

```bash
kubectl get pods

kubectl get pvc
```

Observe that Kubernetes automatically creates:

- mysql-1
- mysql-2
- Dedicated PVCs

---

# 🧪 Verify Stable Identity

Delete one Pod.

```bash
kubectl delete pod mysql-1
```

Wait for recreation.

```bash
kubectl get pods
```

Observe:

```text
mysql-1
```

The Pod keeps the same name.

---

# 🧪 Verify Persistent Storage

Connect to MySQL.

```bash
kubectl exec -it mysql-1 -- mysql -u root -p
```

Use the database.

```sql
USE employee_db;
```

Create a table.

```sql
CREATE TABLE stateful_demo (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

Insert data.

```sql
INSERT INTO stateful_demo VALUES
(1,'StatefulSet Works');
```

Verify.

```sql
SELECT * FROM stateful_demo;
```

Delete the Pod.

```bash
kubectl delete pod mysql-1
```

Reconnect.

```bash
kubectl exec -it mysql-1 -- mysql -u root -p
```

Verify.

```sql
USE employee_db;

SELECT * FROM stateful_demo;
```

The data remains available because the Pod reuses its existing Persistent Volume Claim.

---

# 🔍 Useful Commands

```bash
kubectl get statefulsets

kubectl get pods

kubectl get pvc

kubectl get pv

kubectl get svc

kubectl describe statefulset mysql

kubectl describe pvc

kubectl logs mysql-0

kubectl exec -it mysql-0 -- bash

kubectl scale statefulset mysql --replicas=3

kubectl delete pod mysql-1
```

---

# 📚 Kubernetes Concepts Learned

- StatefulSet
- Headless Service
- Stable Pod Identity
- Stable DNS
- volumeClaimTemplates
- Automatic PVC Creation
- ConfigMap
- Secret
- Persistent Storage
- Ordered Pod Startup
- Ordered Pod Shutdown
- Stateful Applications

---

# 🎯 Learning Outcomes

After completing this project, I gained hands-on experience with:

- Deploying stateful applications using StatefulSets
- Creating Headless Services for stable network identities
- Understanding Pod identity and stable DNS
- Automatically provisioning Persistent Volume Claims using volumeClaimTemplates
- Managing application configuration with ConfigMaps
- Managing sensitive credentials using Secrets
- Scaling StatefulSets while maintaining dedicated storage
- Verifying persistent storage across Pod recreation

---

# 🧠 Key Interview Topics Covered

- Deployment vs StatefulSet
- Stateful Applications
- Headless Service
- ClusterIP vs Headless Service
- Stable DNS
- Stable Pod Identity
- volumeClaimTemplates
- Automatic PVC Creation
- ConfigMap vs Secret
- Persistent Storage
- Ordered Pod Creation
- Ordered Pod Deletion

---

# 📌 Future Improvements

- MySQL Replication
- MySQL Primary-Replica Architecture
- Dynamic Storage Provisioning
- Storage Classes
- Backup & Restore
- MySQL Operator
- Helm Deployment
- Monitoring with Prometheus & Grafana
- TLS-enabled MySQL Communication
- Deploy on Amazon EKS / Azure AKS / Google GKE
