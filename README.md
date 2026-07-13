# minikube_projects
Nginx deployment architecture will look like this:
                Browser
                    │
                    │
            localhost:30080
                    │
            NodePort Service
                    │
          -------------------
          │        │        │
        Pod1     Pod2     Pod3
          │        │        │
           Nginx Container
Step 1: Verify Prerequisites
Run:
docker --version
kubectl version --client
minikube version
If all three work, you're ready.
Step 2: Start Minikube
minikube start
Wait until you see:
Done!
kubectl is now configured to use "minikube".
Step 3: Check the Cluster
kubectl get nodes
Expected:
NAME        STATUS   ROLES           AGE
minikube    Ready    control-plane   2m
Step 4: Create the Project Folder
mkdir kubernetes-projects
cd kubernetes-projects
mkdir project1-nginx
cd project1-nginx
Step 5: Create the Deployment Manifest
Create a file named:
deployment.yaml
Paste this:
apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx-deployment

spec:
  replicas: 3

  selector:
    matchLabels:
      app: nginx

  template:
    metadata:
      labels:
        app: nginx

    spec:
      containers:
      - name: nginx
        image: nginx:latest

        ports:
        - containerPort: 80
This tells Kubernetes:
Create a Deployment named nginx-deployment
Run 3 replicas
Use the official nginx:latest image
Expose port 80 inside each container
Step 6: Apply the Deployment
kubectl apply -f deployment.yaml
You should see:
deployment.apps/nginx-deployment created
Step 7: Verify Pods
kubectl get pods
Expected:
NAME                                READY   STATUS
nginx-deployment-xxxxx              1/1     Running
nginx-deployment-yyyyy              1/1     Running
nginx-deployment-zzzzz              1/1     Running
Step 8: Verify Deployment
kubectl get deployments
Expected:
NAME                READY
nginx-deployment    3/3
Step 9: Expose the Deployment
Create service.yaml:
apiVersion: v1
kind: Service

metadata:
  name: nginx-service

spec:
  type: NodePort

  selector:
    app: nginx

  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30080
Apply it:
kubectl apply -f service.yaml
Step 10: Verify the Service
kubectl get services
Expected output includes:
NAME            TYPE       PORT(S)
nginx-service   NodePort   80:30080/TCP
Step 11: Open the Application
On Minikube:
minikube service nginx-service
or get the URL:
minikube service nginx-service --url
Opening that URL in your browser should display the default Welcome to nginx! page.
Step 12: Scale the Deployment
Increase replicas:
kubectl scale deployment nginx-deployment --replicas=5
Check:
kubectl get pods
You should now see 5 running Pods.
Step 13: Inspect the Deployment
Useful commands:
kubectl describe deployment nginx-deployment
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl get all
Step 14: Clean Up
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
