pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				sh '''ls -l  && cd evolution && python3 manage.py test'''
			}	
		}
		stage('Docker-push') {
			steps {
				app = docker.withRegistry('https://hub.docker.com/repository/docker/chljidn/evolution','docker_hub')
			}
		}
	}
}

