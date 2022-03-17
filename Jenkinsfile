pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				sh '''ls -l  && cd evolution && python3 manage.py test && cd ..'''
			}	
		}
	}
	
		stage('Docker-compose') {
			steps {
				sh 'docker-compose build'				
			}
			
		}
}

