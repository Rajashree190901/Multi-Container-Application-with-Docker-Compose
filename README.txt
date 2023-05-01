MULTI CONATINER - APPLICATION -WITH -DOCKER-COMPOSE

This is a multi-container Docker application with a front-end in Python and a database in MySQL. The front-end application allows users to enter a student registration number and get their COVID vaccination status from the database.

INSTALLATION AND USAGE:
* I have installed docker desktop and visual studio code to run the application.
* Navigate to the root directory of the project.
* i have Build the Docker images and started the containers by running the following command:  docker-compose up -d
* Once the containers are up and running, we can access the front-end application by opening your web browser and navigating to http://localhost:5000.
* By Enter a student registration number and clicking the "Tab to get Vaccination Status" button. The application will query the MySQL database and display the student's vaccination status.
* To stop the containers, run the following command:docker-compose down

DOCKER  COMPOSE CONFIGUARTION
* The docker-compose.yml file in the root directory of the project defines the configuration for the Docker Compose application. It specifies two services: frontend and database.
* The frontend service uses the Dockerfile in the ./frontend directory to build a Docker image based on the python:3.8-alpine base image. It exposes port 5000 and mounts the ./frontend directory as a volume.
* The database service uses the mysql:latest image from Docker Hub to create a MySQL database container. It sets the MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, and MYSQL_USER environment variables to configure the database. It also mounts the ./database directory as a volume to persist the data.

MySQL DATABASE
* The MySQL database is initialized with a students table that contains the following columns: id, registration_number, name, and vaccination_status. The database is pre-populated with sample data for testing purposes.

FRONT-END APPLICATION
* The front-end application is a simple Python Flask app that serves an HTML form to the user. When the user submits the form, the app sends a request to the back-end API to get the student's vaccination status from the database.





