pipeline {
    agent any

    environment {
        PYTHON_HOME = "C:/Users/Haris Usman/AppData/Local/Programs/Python/Python310" // Update the path with forward slashes
        DOCKER_IMAGE_TAG = "my-notebook-image"
        DOCKER_CONTAINER_NAME = "my-notebook-container"
    }

    stages {
        stage("Stage 1: Installing Dependencies") {
            steps {
                echo "Installing dependencies..."
                bat "\"${PYTHON_HOME}/Scripts/pip.exe\" install black"
                bat "\"${PYTHON_HOME}/Scripts/pip.exe\" install autopep8"
            }
        }

        stage("Stage 2: Code Formatting") {
            steps {
                echo "Running black..."
                bat "\"${PYTHON_HOME}/Scripts/black.exe\" ." // Replace 'your-black-command-here' with '.' to format all files in the current directory
            }
        }

        stage("Stage 3: Reviewing Code for Improvements") {
            steps {
                echo "Running autopep8..."
                bat "\"${PYTHON_HOME}/Scripts/autopep8.exe\" --in-place --recursive ." // Replace 'your-autopep8-command-here' with '--in-place --recursive .' to recursively format all files in the current directory
            }
        }

        stage("Stage 4: Build Docker Image") {
            steps {
                echo "Building Docker image..."
                bat "docker build -t ${DOCKER_IMAGE_TAG} ."
            }
        }

        stage("Stage 5: Run Docker Container") {
            steps {
                echo "Running Docker container..."
                bat "docker run -p 8888:8888 --name ${DOCKER_CONTAINER_NAME} ${DOCKER_IMAGE_TAG}"
            }
        }
    }
}
