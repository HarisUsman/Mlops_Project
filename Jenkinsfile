pipeline {
    agent any
    environment {
        PYTHON_HOME = "C:/Users/Haris Usman/AppData/Local/Programs/Python/Python310" // Update the path with forward slashes
    }
    stages {
        stage("Stage 1: Installing Dependencies") {
            steps {
                echo "Installing dependencies..."
                bat "\"${PYTHON_HOME}/Scripts/pip.exe\" install black[jupyter]"
                bat "\"${PYTHON_HOME}/Scripts/pip.exe\" install autopep8"
            }
        }
        stage("Stage 2: Code Formatting") {
            steps {
                echo "Running black..."
                bat "\"${PYTHON_HOME}/Scripts/black.exe\" ."
            }
        }
        stage("Stage 3: Reviewing Code for Improvements") {
            steps {
                echo "Running autopep8..."
                bat "\"${PYTHON_HOME}/Scripts/autopep8.exe\" --in-place --recursive ."
            }
        }
    }
}
