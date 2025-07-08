# 20CYS402 - Distributed Systems and Cloud Computing
![](https://img.shields.io/badge/Batch-22CYS-lightgreen) ![](https://img.shields.io/badge/UG-blue) ![](https://img.shields.io/badge/Subject-DSCC-blue) <br/>

## Resource for Lab 1: Creating a Docker image and pushing to Docker Hub
![](https://img.shields.io/badge/04_Jul-blue) ![](https://img.shields.io/badge/08_Jul-darkred)

### Creating a Docker image 

#### 🧰 Prerequisites

- Install Docker Desktop:  
  [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- Basic understanding of Linux commands

---

#### 📁 1. Create a Project Directory in you Host Machine 

```
mkdir dockerlab
cd dockerlab
```

Add your application files (e.g., Python, Node.js, etc.) inside this directory.

---

#### 📝 2. Create a Dockerfile

Inside `dockerlab/`, create a file named `Dockerfile` (no extension).

Example for a **Python app**:

```
# Use an official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the app
CMD ["python", "app.py"]
```

---

#### ⚙️ 3. Create Requirements File (for Python Apps)

Inside the same folder, create `requirements.txt` with your dependencies:

```
flask
requests
```

Also, create a sample `app.py` if not already present.

---

#### 🛠️ 4. Build the Docker Image

Run this command from inside the folder (where the Dockerfile is):

```
docker build -t myapp-image .
```

Explanation:
- `-t myapp-image`: Name/tag of the image
- `.`: The current directory as build context

---

#### 📦 5. Run a Container from the Image

```
docker run -d -p 5000:5000 myapp-image
```

Explanation:
- `-d`: Run in detached mode
- `-p 5000:5000`: Map container port to host port

---

#### 🔍 6. Verify Everything is Working

Check the running container:

```
docker ps
```

Open your browser:  
➡️ `http://localhost:5000`

---

#### 🧹 7. Clean Up (Optional)

Stop container:

```
docker stop <container_id>
```

Remove container:

```
docker rm <container_id>
```

Remove image:

```
docker rmi myapp-image
```

---

#### ✅ Summary Steps

1. Make a project folder  
2. Add a `Dockerfile`, app code, and dependencies  
3. Run `docker build`  
4. Run the image using `docker run`

### 🐳 How to Push a Docker Image to Docker Hub

---

#### 🔐 1. Login to Docker Hub

Make sure you have a Docker Hub account. Then log in from your terminal:

```
docker login
```

Enter your **Docker Hub username** and **password** when prompted.

---

#### 🏷️ 2. Tag Your Image Properly

Docker requires the image to be tagged in the format:

```
<dockerhub-username>/<repository-name>:<tag>
```

Example:

```
docker tag myapp-image ramgurur/myapp:latest
```

Here:
- `myapp-image` is your local image name
- `ramgurur/myapp` is the Docker Hub repository (replace `ramguru` with your Docker Hub username)
- `latest` is the tag (can be any version string like `v1`, `v2.0`, etc.)

---

#### 📤 3. Push the Image to Docker Hub

```
docker push ramgurur/myapp:latest
```

---

#### 🧪 4. Verify the Image on Docker Hub

1. Go to [https://hub.docker.com](https://hub.docker.com)
2. Log in
3. Navigate to your repositories
4. You should see your image `myapp` with the `latest` tag

---

#### 🧹 5. Optional: Remove Local Image

If you want to save space:

```
docker rmi myapp-image
docker rmi ramgurur/myapp:latest
```

---

#### ✅ Quick Summary

1. `docker login`
2. `docker tag <image> <username>/<repo>:<tag>`
3. `docker push <username>/<repo>:<tag>`
