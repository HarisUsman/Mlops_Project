pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/HarisUsman/Mlops_Project.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'mvn clean install' // Replace with your build command
            }
        }
        
        stage('Test') {
            steps {
                sh 'mvn test' // Replace with your test command
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker build -t your-image:tag .' // Replace with your deploy command
                sh 'docker push your-image:tag' // Replace with your deploy command
            }
        }
    }
}
