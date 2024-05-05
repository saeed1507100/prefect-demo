# Prefect Cloud Demo

## 1. Getting started
### 1.1 Install prefect
```bash
pip install prefect
```

### 1.2 Connect to prefect cloud
```bash
prefect cloud login
```
We will be prompted to login with API Key or with Web browser. We can simply do it using web browser.

### 1.3 Create deployment
Run flows/hello_world.py to create a deployment of simple flow hello_world.
You can see the deployment in the prefect cloud.
You can tweak the parameters of deployment to explore more.
```bash
python flows/hello_world.py
```

### 1.4 Run deployment    
From Prefect cloud UI, when you run the deployment, it will execute directly on the terminal.

## 2. Worker-pools
### 2.1 Create worker-pool: subprocess
From prefect cloud UI `Work Pools` tab, you can create a worker-pool with the `+` button.
![Screenshot 2024-05-05 at 7.13.15 AM.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2F4k%2Fdwql3nfj2yjdrgnnddxpfr740000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_o7WfbT%2FScreenshot%202024-05-05%20at%207.13.15%E2%80%AFAM.png)
Select `Infrastructure type`: `Local Subprocess`, give a name (e.g. `workpool-process-demo`), description & concurrency limit.
In the next page, set the working directory to the root of the project & create the worker-pool.

#### Start a worker in that pool
```bash
prefect worker start --pool "workpool-process-demo"
```

#### Run deployment in worker-pool
From Prefect cloud UI, configure the deployment worker pool to `workpool-process-demo`. 
When you run the deployment, it will submit to the worker-pool. 
The running worker (local subprocess) will pick up the deployment and execute it.

#### Stop worker
We can stop the worker using `control + c` in the terminal. 
The worker will be visible as offline in Work-pool page of prefect cloud UI.

### 2.2 Create worker-pool: GCP Cloud Run

#### Create a new project in GCP
Create a new project in GCP and enable Cloud Run API.
Create a service account with `Cloud run admin` role & `iam.ServiceAccount.actAs` permission to the default compute engine service account.
Download the service account key as json.

#### Create a docker image
Create a docker image with the Dockerfile.
```bash
docker buildx build -t [dockerhub_username]/[image_name]:[tag] --platform=linux/amd64 .
```
login to dockerhub. put your dockerhub username & password.
```bash
docker login
```

Push the image to dockerhub.
```bash
docker push [dockerhub_username]/[image_name]:[tag]
```

#### Create a worker-pool in Prefect cloud
From prefect cloud UI `Work Pools` tab, you can create a worker-pool with the `+` button.
Select `Infrastructure type`: `GCP Cloud Run`, give a name (e.g. `workpool-cloudrun-demo`), description & concurrency limit.
In the next page, 
- Set GCP credentials using GCP Service account key file
- set the image location: `docker.io/[dockerhub_username]/[image_name]:[tag]`
- We can keep the CPU & Memory limits as default.
- Create the worker-pool.

#### Start a worker in that pool
It may take some time cause it will install prefect-gcp package.
```bash
prefect worker start --pool "gcp-cloud-run-workpool-demo"
```

#### Run deployment in worker-pool
Edit any deployment & set worker-pool to `gcp-cloud-run-workpool-demo`. 
When you run the deployment, it will submit to the worker-pool.
In GCP cloud run console, you can see the prefect Job running.


