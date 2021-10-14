pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Run tests') {
            steps {
                echo 'Running tests'
                bat 'python -m pytest'
            }
        }
    }
}