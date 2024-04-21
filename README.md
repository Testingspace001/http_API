0) # http_API
Equal expert Project

1) # Building an API, testing it, and packaging it into a container
This project aims to guide you through the process of building an HTTP API application, testing it, and packaging it into a container. By following the steps outlined below, you'll be able to create a simple HTTP API application using a Python code. You will also be able to test its functionality and, finally, containerise it into a Docker image using a Dockerfile for easy deployment.

2) # Prerequisites:
Before getting started, we ensured the following is installed:

* Visual Studio Code
* Git Bash
* MobaXterm
* Git
* Docker
* Python 3.9
* Flask 2.6.0

3) # Installation

  * In our local enviroment, Git Bash, MobaXterm and Visual Studio Code were installed.
  * An EC2 instance was created in Linux Redhat where Git, Docker, Python 3.9 and Flask were installed using the following commands:
     - sudo yum update  # This will update our linux Redhat packages 
     - sudo yum install git # Git installation 
     - sudo yum install python3 # Python installation
     - sudo yum install python3-pip # Installing Python Package manager (Pip)
     - sudo pip3 install Flask #Installing Flask (Python dependency)
       
     - The following commands will install Docker:
        # !/bin/bash
        # Update the package index
        sudo yum update -y
        sudo yum install -y yum-utils device-mapper-persistent-data lvm2 # Install required dependencies
        sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo # Set up the Docker repository
        sudo yum install -y docker-ce docker-ce-cli containerd.io # Install Docker
        sudo systemctl start docker # Start Docker service
        sudo systemctl enable docker # Enable Docker to start on boot
        sudo usermod -aG docker $(whoami) # Add the current user to the docker group to run Docker commands without sudo
        docker --version # Display Docker version

4) # Creation of required Files
In our enviroment, Five (5) files were created using Vitual Studio Code including: 
- Dockerfile             # The file used to containerise the application.
- Http_Api.py            # The HTTP API source code in Python. 
- Test_Http_api.py       # The file used to test the HTTP API application.
- requirements.txt       # File containing all the needed dependencies.
- README.md              # The file containing the step by step procedures on the HTTP API Application creation and testing.

5) # All the above files, were pushed from our local repository to a remote repository (GitHub) using Git Bash

6) # Containerisation
   The repository containing our files was cloned into our server using 'git clone' command.
   
   We packaged the API into a Docker container using the Dockerfile by running the following command:
      docker build -t api-image .

   The application was run in docker using the following command:
      docker run --name api -d -p 8080:8080 api-image

7) # Testing
   The application was tested by accessing it via the web browser using the public IP of our server mapped to the Port 8080.
   
   We ensured that Port 22 used to SSH, and Port 8080, used to access our application, were opened in our firewall inbound rules.



     




