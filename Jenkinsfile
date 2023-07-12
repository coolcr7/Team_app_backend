pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from version control system (e.g., Git)
                git 'https://github.com/coolcr7/Team-app.git'
            }
        }
        stage('Dockerize') {
            steps {
                // Build Docker image for your frontend application
                sh 'docker build -t chaya01/frontend-app .'
                // Tag the image with your Docker Hub username and repository name
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                // Push the Docker image to Docker Hub
                sh 'docker login -u chaya01 -p Riya@0112'
                // Login to Docker Hub using your credentials
                
                sh 'docker push chaya01/frontend-app'
                // Push the image to Docker Hub repository
            }
        }
    }
}

