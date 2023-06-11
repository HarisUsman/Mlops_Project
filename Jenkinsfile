pipeline {
    agent any
    environment {
        PATH = "${tool 'Python'}/Scripts:${env.PATH}"
    }
    stages {
        stage("Stage 1: Installing Dependencies") {
            steps {
                echo "Installing dependencies..."
                bat "pip install black"  
                bat "pip install autopep8"
            }
        }
        stage("Stage 2: Code Formatting") {
            steps {
                echo "Running black..."
                bat "black your-black-command-here"
            }
        }
        stage("Stage 3: Reviewing Code for Improvements") {
            steps {
                echo "Running autopep8..."
                bat "autopep8 your-autopep8-command-here"
            }
        }
    }
}
