pipeline {
    agent any
    stages {
        stage("Stage 1: Installing Dependencies") {
            steps {
                echo "Installing dependencies..."
                bat "\"${tool 'Python'}/Scripts/pip.exe\" install black"
                bat "\"${tool 'Python'}/Scripts/pip.exe\" install autopep8"
            }
        }
        stage("Stage 2: Code Formatting") {
            steps {
                echo "Running black..."
                bat "\"${tool 'Python'}/Scripts/black.exe\" your-black-command-here"
            }
        }
        stage("Stage 3: Reviewing Code for Improvements") {
            steps {
                echo "Running autopep8..."
                bat "\"${tool 'Python'}/Scripts/autopep8.exe\" your-autopep8-command-here"
            }
        }
    }
}
