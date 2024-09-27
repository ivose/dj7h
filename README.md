
# Project Setup Instructions

## Recommended Setup

It is recommended to use a Linux operating system, or if you're on Windows, use WSL (Windows Subsystem for Linux) with an Ubuntu installation. 

Ensure that Docker is installed with **version 26.0.0** and Docker Compose with **version v2.29.3**. Other versions may cause issues during the setup process.

## Steps to Set Up the Project

1. Clone the repository by running the following command:

    ```bash
    git clone https://github.com/ivose/dj7h
    ```

2. Navigate to the project directory:

    ```bash
    cd dj7h
    ```

3. Create file .env and copy .env_example to it and give own values, you can also do a commnad:

    ```bash
    cp .env_example .env
    ```

4. Run the following command to build and start the containers:

    ```bash
    docker-compose up -d --build --remove-orphans
    ```

5. It's recommended to create also an admin user with a command:

    ```bash
    docker-compose run d7h-web python manage.py createsuperuser
    ```

6. The project should now be up and running. Check if everything works correctly.
