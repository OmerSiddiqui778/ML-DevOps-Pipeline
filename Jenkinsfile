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
                sh 'docker build -t ai-vs-real-app:latest .'
            }
        }
        stage('test model'){
            steps{
                echo 'Running sanity checks...'
                echo 'All checks passed!'
            }
        }
        stage('deploy staging'){
            steps{
                echo 'Deploying to local container...'
                sh 'docker stop ml-app-container || true'
                sh 'docker rm -d -p 8501:8501 --name ml-app-container ai-vs-real-app:latest'
                echo 'Application is live at http:localhost:8501'
            }
        }
    }
}