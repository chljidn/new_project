pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				sh '''ls -l  && cd evolution && python3 manage.py test'''
			}	
		}
		stage('
		
		stage('Docker-push') {
			steps {
				sh echo credentials('docker-hub')
			}
		}
	}
}

