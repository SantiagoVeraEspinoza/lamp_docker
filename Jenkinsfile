pipeline {
    agent any

    environment {
        COMPOSE_FILE_PATH = './' // Path to your docker-compose.yml file, if not in the root directory
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the Git repository
                dir(COMPOSE_FILE_PATH) {
                    sh 'git checkout main; git reset --hard; git pull' // Specify the branch to checkout
                }
            }
        }
        
        stage('Stop Docker Compose') {
            steps {
                // Navigate to the directory where docker-compose.yml is located
                dir(COMPOSE_FILE_PATH) {
                    // Run docker-compose down to stop the running services
                    sh 'docker-compose down'
                    sh 'sleep 3'
                }
            }
        }
        
        stage('Start Docker Compose') {
            steps {
                // Navigate to the directory where docker-compose.yml is located
                dir(COMPOSE_FILE_PATH) {
                    // Run docker-compose up to start the services
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
