pipeline {
	agent any
	environment {
		DOCKER_HUB_ID = credentials('docker_hub-username')
		DOCKER_HUB_PASSWD = credentials('docker_hub-password')
	}
	stages {
		stage('Test') {
			steps {
				sh '''ls -l  && cd evolution && python3 manage.py test'''
			}	
		}
		stage('Docker-push') {
			steps {
				sh 'echo $DOCKER_HUB_ID'
			}
		}
	}
}

