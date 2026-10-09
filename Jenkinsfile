pipeline{
    agent any
    environment{
        TAG = "${env.BUILD_NUMBER}"
    }
    stages{
        stage('Build'){
            steps{
                bat 'docker compose build'
            }
        }
        stage('Test'){
            steps{
                bat "docker run --rm gopimano1997/cn-backend:%TAG% pytest"
            }
        }
        stage('Push') {
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]){
                    bat 'echo %PASS%| docker login -u %USER% --password-stdin'
                    bat 'docker compose push gopimano1997/cn-backend:%TAG%'
                    bat 'docker compose push gopimano1997/cn-frontend:%TAG%'
                }
            }
        }
        stage('Deploy'){
            steps{
                withCredentials([string(credentialsId: 'cn-db-password', variable: 'DB_PASS')]){
                    bat 'echo POSTGRES_PASSWORD=%DB_PASS%> db.env'
                    bat 'echo DB_PASSWORD=%DB_PASS%>> db.env'
                    bat 'docker compose -p cartnova-store up -d'
                }
            }
        }
        stage('Smoke test'){
            steps{
                sleep 5
                bat 'curl -f http://localhost:5000/health'
                bat 'curl -f http://localhost:5000/api/products'
                bat 'curl -f http://localhost:8080'
            }
        }
    }
    post{
        always {bat 'if exist db.env del db.env'}
    }
}