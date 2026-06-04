pipeline {
    agent any

    stages {
        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        
        stage('Build Image') {
            steps {
                echo 'Building the Docker container application artifact...'
                bat "docker build -t ai-vs-real-app:latest ."
            }
        }

        
        stage('Test Model') {
            steps {
                echo 'Running automated Python test suite inside the container...'
                bat "docker run --rm ai-vs-real-app:latest pytest test_app.py"
            }
        }

        
        stage('Code Quality Analysis') {
            steps {
                echo 'Running codebase health and maintainability analysis...'
                
                bat "docker run --rm ai-vs-real-app:latest radon cc app.py test_app.py -s"
            }
        }

        
        stage('Deploy Staging') {
            steps {
                echo 'Deploying application container to local staging server...'
                
                bat "docker stop ai-vs-real-container || true"
                bat "docker rm ai-vs-real-container || true"
                
                
                bat "docker run -d -p 8501:8501 --name ai-vs-real-container ai-vs-real-app:latest"
                echo 'Application successfully deployed live to http://localhost:8501'
            }
        }
    }
}