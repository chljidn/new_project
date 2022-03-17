pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				sh '''ls -l  && cd evolution && python3 manage.py test'''
			}	
		}
	
	
		stage('Docker-build') {
			steps {
				sh 'docker build chljidn/evolution:evolution'				
			}
			
		}
	}
}

