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
                                sh 'cd evolution && docker build . -t chljidn/evolution:evolution'
                        }
                }
		stage('Docker-login') {
			steps {
				sh 'echo $DOCKER_HUB_PSW | docker login -u $DOCKER_HUB_USR --password-stdin'
			}
		}
		stage('Docker-push') {
			steps {
				sh 'docker push chljidn/evolution:evolution'
			}
		}
		stage('Docker-rmi') {
			steps {
				sh 'docker rmi chljidn/evolution:evolution'
			}
		} 
	}
}

