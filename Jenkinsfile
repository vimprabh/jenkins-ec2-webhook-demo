cat > Jenkinsfile <<'EOF'
pipeline {

    agent any

    triggers {
        githubPush()
    }

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Application') {
            steps {
                sh 'python3 hello.py'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }
    }

    post {

        success {
            emailext(
                to: 'vimal.prabhakaran@gmail.com',
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                Jenkins Build Successful!

                Job: ${env.JOB_NAME}
                Build: ${env.BUILD_NUMBER}
                Status: SUCCESS

                Build URL: ${env.BUILD_URL}
                """
            )
        }

        failure {
            emailext(
                to: 'vimal.prabhakaran@gmail.com',
                subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                Jenkins Build Failed!

                Job: ${env.JOB_NAME}
                Build: ${env.BUILD_NUMBER}
                Status: FAILURE

                Check Jenkins logs:
                ${env.BUILD_URL}
                """
            )
        }
    }
}
