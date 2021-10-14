pipeline {
    agent any

    stages {
        stage('Hello') {
            echo 'Hello World'
        }
        stage('Run tests') {
            echo 'Running pytests'
            def run_test_command = 'python -m pytest'
            bat '${run_test_command}'
        }      
    }
}