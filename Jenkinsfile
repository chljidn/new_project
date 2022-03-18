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
				sh 'cd evolution'
			}
			app = docker.build('chljidn/evolution')
		}
		stage('Docker-push') {
			steps {
				docker.withRegistry('https://registry.hub.docker.com', 'docker_hub') {
				app.push('${env.BUILD_NUMBER}')
				app.push('letest')	

				}
			}
		}
	}
}

