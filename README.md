# HORC-Elections

HORC-Elections is a web application designed for conducting elections within the HORC (House of Representatives Council) community. This README provides instructions for developers on how to set up and run the project, as well as important information about the project's architecture and environment variables.


## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine using the following command:

   ```shell
   git clone https://github.com/DaemonLab/HORC-Elections
   ```
By default, SQLite is used as the database during development. You can run the project with this configuration. However, for production, you should configure a more robust database like MySQL or PostgreSQL.

## Running the Project

You have two options for running the project: using standard Django management commands or Docker Compose.

### Option 1: Standard Django

To run the project using standard Django management commands, follow these steps:

1. Navigate to the project directory in your terminal.

2. Apply the database migrations:

   ```shell
   python manage.py migrate
   ```

3. Start the development server:

   ```shell
   python manage.py runserver
   ```

4. Access the application in your web browser at `http://localhost:8000`.

### Option 2: Docker Compose

To run the project using Docker Compose, make sure you have Docker and Docker Compose installed. Then, follow these steps:

1. Navigate to the project directory in your terminal.

2. Create a `.env` file in the project directory and configure the necessary environment variables. You can use the provided `.env.example` file as a template.

3. Build and start the Docker containers:

   ```shell
   docker-compose up
   ```

4. Access the application in your web browser at `http://localhost:8000`.

## Environment Variables

To configure your project's environment variables, create a `.env` file in the project directory or set the necessary environment variables manually. You can use the `.env.example` file as a reference for the required variables.

Ensure that your environment variables are correctly set for your specific development or production environment.

## Project Schema

Below is the project schema for better understanding:

![Project Schema](https://github.com/DaemonLab/HORC-Elections/assets/72644006/fb77d48f-c859-4236-a59c-540154e84ba1)

Feel free to reach out to the project maintainers for any further assistance or inquiries.