pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t yourusername/wog:latest .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 -v $(pwd)/Scores.txt:/Scores.txt --name wog-test yourusername/wog:latest'
            }
        }
        stage('Test') {
            steps {
                sh 'python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker stop wog-test'
                sh 'docker rm wog-test'
                sh 'docker login -u yourusername -p yourpassword'
                sh 'docker push yourusername/wog:latest'
            }
        }
    }
}