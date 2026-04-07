
## Project Overview

This project demonstrates a complete DevOps deployment pipeline from local development to cloud deployment.

Tech stack:

- Frontend: HTML, CSS, JavaScript
- Backend: Node.js + Express
- Database: SQLite
- Containerization: Docker
- Container Registry: Docker Hub
- Cloud Deployment: Azure Kubernetes Service (AKS)

## What We Implemented

1. Built and tested a working full-stack Notes app locally.
2. Added Dockerfile and containerized the app.
3. Built a custom Docker image and ran it in a container.
4. Pushed image to Docker Hub.
5. Created AKS cluster on Azure student subscription.
6. Deployed Docker Hub image on AKS.
7. Exposed app using LoadBalancer service and public IP.
8. Used Git/GitHub workflow for version control.

## Application Features

- Add note
- View all notes
- Delete note

## Local Run Steps

1. Install Node.js.
2. Run `npm install`.
3. Run `npm start`.
4. Open `http://localhost:3000`.

## Docker Steps

1. Build image:

```bash
docker build -t notes-app:v1 .
```

2. Run container:

```bash
docker run -d --name notes-container -p 3000:3000 notes-app:v1
```

3. Verify running container:

```bash
docker ps -a
```

## Docker Hub Steps

1. Login:

```bash
docker login
```

2. Tag and push image:

```bash
docker tag notes-app:v1 abdulmateen014/notes-app:v1
docker push abdulmateen014/notes-app:v1
```

3. Pull verification:

```bash
docker pull abdulmateen014/notes-app:v1
```

Docker Hub image:

- `abdulmateen014/notes-app:v1`
- `https://hub.docker.com/repository/docker/abdulmateen014/notes-app/general`

## AKS Deployment Steps

1. Open Azure Cloud Shell.
2. Set subscription and connect AKS:

```bash
az account set --subscription 43706bb3-d911-4f11-a47c-8839d2c0e5e6
az aks get-credentials --resource-group RG-LabMid-AKS --name aks-labmid-demo --overwrite-existing
kubectl get nodes
```

3. Apply deployment manifest:

```bash
kubectl apply -f aks-deploy.yaml
kubectl get pods
kubectl get svc notes-app-service
```

4. Use external IP to access the app.

Azure public URL:

- `http://85.211.202.215`


```


