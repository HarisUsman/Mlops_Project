pipeline {
    agent any
    environment {
        PYTHON_HOME = "C:\\path\\to\\python" // Set the path to your Python installation directory
    }
    stages {
        stage("Stage 1: Installing Dependencies") {
            steps {
                echo "Installing dependencies..."
                bat "\"%PYTHON_HOME%\\Scripts\\pip.exe\" install black"
                bat "\"%PYTHON_HOME%\\Scripts\\pip.exe\" install autopep8"
            }
        }
        stage("Stage 2: Code Formatting") {
            steps {
                echo "Running black..."
                bat "\"%PYTHON_HOME%\\Scripts\\black.exe\" your-black-command-here"
            }
        }
        stage("Stage 3: Reviewing Code for Improvements") {
            steps {
                echo "Running autopep8..."
                bat "\"%PYTHON_HOME%\\Scripts\\autopep8.exe\" your-autopep8-command-here"
            }
        }
    }
}
