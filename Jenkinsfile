pipeline{
    agent any 
    
    stages {
        stage("Checkout"){
            steps{
                checkout scm 
            }
        }
        stage("Build image"){
            steps{
                echo "builing the docker image...."
                bat 'docker build -t ai-vs-real-app:latest .'
            }
        }
        stage('test model'){
            steps{
                echo 'Running manual ML sanity checks...'
                bat 'docker run --rm ai-vs-real-app:latest pytest test_app.py'
                echo 'All checks passed!'
            }
        }
        stage('deploy staging'){
            steps{
                echo 'Deploying the streamlit app to local container...'
                bat 'docker stop ml-app-container || exit 0'
                bat 'docker rm ml-app-container || exit 0'
                bat 'docker run -d -p 8501:8501 --name ml-app-container ai-vs-real-app:latest'
                echo 'Application is live at http:localhost:8501'
            }
        }
    }
}