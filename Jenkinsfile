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
				sh echo 'docker_hub'
				app = docker.withRegistry('https://registry.hub.docker.com','docker_hub')
			}
		}
	}
}

