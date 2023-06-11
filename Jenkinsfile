pipeline {
    agent any
    tools {
        // Specify the configured Python tool name
        // Adjust 'Python' to match the configured tool name in Jenkins Global Tool Configuration
        python 'Python'
    }
    stages {
        stage("Stage 1: Installing Dependencies") {
            steps {
                echo "Installing dependencies..."
                sh "pip install black"  
                sh "pip install autopep8"
            }
        }
        stage("Stage 2: Code Formatting") {
            steps {
                echo "Running black..."
                sh "black your-black-command-here"
            }
        }
        stage("Stage 3: Reviewing Code for Improvements") {
            steps {
                echo "Running autopep8..."
                sh "autopep8 your-autopep8-command-here"
            }
        }
    }
}
