pipeline {
    agent any
    environment {
        PYTHON_HOME = "C:\\Users\\Haris Usman\\AppData\\Local\\Programs\\Python\\Python310"
    }
    stages {
        stage("Stage 1: Installing Dependencies") {
            steps {
                echo "Installing dependencies..."
                bat "${PYTHON_HOME}\\python.exe -m pip install black"
                bat "${PYTHON_HOME}\\python.exe -m pip install autopep8"
            }
        }
        stage("Stage 2: Code Formatting") {
            steps {
                echo "Running black..."
                build job: 'jobone', parameters: [
                    string(name: 'PYTHON_HOME', value: PYTHON_HOME)
                ]
            }
        }
        stage("Stage 3: Reviewing Code for Improvements") {
            steps {
                echo "Running autopep8..."
                build job: 'jobtwo', parameters: [
                    string(name: 'PYTHON_HOME', value: PYTHON_HOME)
                ]
            }
        }
    }
}
