pipeline {
    agent any
    stages {
        stage("Stage 1: Installing Dependencies") {
            steps {
                echo "Installing dependencies..."
                sh "pip3 install black"  
                sh "pip3 install autopep8"
            }
        }
        stage("Stage 2: Code Formatting") {
            steps {
                echo "Running black..."
                sh "your-black-command-here"
            }
        }
        stage("Stage 3: Reviewing Code for Improvements") {
            steps {
                echo "Running autopep8..."
                sh "your-autopep8-command-here"
            }
        }
    }
}
