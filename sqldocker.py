import sys
import yaml
import subprocess
import os

# Define the path to the docker-compose directory
COMPOSE_DIR = 'mysqlbcit'
COMPOSE_FILE = os.path.join(COMPOSE_DIR, 'docker-compose.yml')
ENV_FILE = os.path.join(COMPOSE_DIR, '.env')

def run_mysql_container():

    # Run Docker Compose to start the MySQL container
    try:
        subprocess.run(['docker-compose', '-f', COMPOSE_FILE, 'up', '-d'], check=True)
        print("MySQL container started.")
    except subprocess.CalledProcessError:
        print("Error starting MySQL container with Docker Compose.")

def close_mysql_container(remove_image=False):
    # Stop and remove the MySQL container along with images and volumes if specified
    command = ['docker-compose', '-f', COMPOSE_FILE, 'down']

    if remove_image:
        command.extend(['--rmi', 'all', '-v'])

    try:
        subprocess.run(command, check=True)
        print("MySQL container stopped and removed.")
    except subprocess.CalledProcessError:
        print("Error stopping MySQL container with Docker Compose.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "close":
        close_mysql_container()
    elif len(sys.argv) > 1 and sys.argv[1] == "drop":
        close_mysql_container(remove_image=True)
    else:
        run_mysql_container()