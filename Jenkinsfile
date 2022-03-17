pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				sh '''ls -l  && cd evolution && ls -l && python3 manage.py test'''
			}	
		}
	}
}

