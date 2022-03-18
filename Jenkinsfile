pipeline {
	agent any
	environment {
		DOCKER_HUB_ID = credentials('chljidn')
	}
	stages {
		stage('Test') {
			steps {
				sh '''ls -l  && cd evolution && python3 manage.py test'''
			}	
		}
		stage('Docker-push') {
			steps {
				sh echo ${env.DOCKER_HUB_ID}
			}
		}
	}
}

