# 20CYS402 - Distributed Systems and Cloud Computing
![](https://img.shields.io/badge/Batch-22CYS-lightgreen) ![](https://img.shields.io/badge/UG-blue) ![](https://img.shields.io/badge/Subject-DSCC-blue) <br/>

## Lab 1: Creating a Docker image and pushing to Docker Hub
![](https://img.shields.io/badge/04_Jul-blue) ![](https://img.shields.io/badge/08_Jul-darkred)

### Docker 

Docker is 
- a software platform where
  - build,
  - test,
  - deploy applications quickly.
- packages software into standardized units called containers
- these containers have everything the software needs to run
  - libraries,
  - system tools,
  - code,
  - runtime
 
<p align="center">
  <img src="https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/containers/approved/images/2e5f22ba-2678-4df9-af45-7e575f5d5590.801e619624462059ed2678866fd430490d521208.png" width=600 />
</p>

### Docker Examples
- [Simple Dockerfile Building](https://www.youtube.com/watch?v=0HCBQpfQE7o)
- [Demo Dockerfile Building](https://www.youtube.com/watch?v=lrTBwlW46Ik)
- [Demo Image Running](https://www.youtube.com/watch?v=ND-qkZVc3KM)
- [Pushing Image to DockerHub](https://www.youtube.com/watch?v=pBdN1OlWGQc)

### Practice Exercise

- The base layer is "alpine"
- Set a Environmental Variable called "ROLLNO" to your full roll number (CB.EN.U4CYS220YY)
- Make a directory called "DSCC"
- Change Directory to "DSCC"
- Create a file called "Lab1.txt" and write your DockerHub username to it
- Upload the image to the DockerHub

### Assignment
Create a Docker Image for a Database Connector.

####  Objective:
Build a Docker image for a database connector application. The application connects to a database using a specific programming language and requires the installation of certain packages. Set environment variables for database connection details and expose the application on a specific IP address and port.

#### Requirements:
 - Choose a base image appropriate for the chosen programming language (e.g., Python, Node.js, Ruby).
 - Install the necessary packages for connecting to a database. Choose a simple database connector library compatible with your chosen language (e.g., psycopg2 for Python, mysql2 for Node.js, pg for Ruby).
 - Set environment variables for the following database connection details:
   - Database host
   - Database port
   - Database username
   - Database password
   - Database name
 - Expose the application on a specific IP address and port (e.g., IP: 0.0.0.0, Port: 8080).
 - Create a sample application code that uses the installed database connector library to connect to a database (you can use dummy values for the connection).

#### Tips:
 - Use an official base image related to the chosen programming language.
 - Clearly document each step in the Dockerfile using comments.
 - Make sure to expose the correct port for your application.
 - Test the Docker image locally to ensure the database connector application is running.

#### Submission:
Provide the following in your submission:
 - The Dockerfile used to build the Docker image.
 - The source code of the sample application demonstrating the database connection.
 - Link to Image in Docker Hub.


