pipeline {

	agent any
	environment {
		DOCKER_HUB=credentials('docker_hub')
	}
	stages {
		stage('Test') {
			steps {
				sh '''ls -l  && cd evolution && python3 manage.py test'''
			}	
		}
		stage('Docker-build') {
			steps {
				sh 'echo $DOCKER_HUB_USR && echo $DOCKER_HUB_PSW'
			}
		}
	}
}

