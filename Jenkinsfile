pipeline {
    agent {
    	docker { image 'python:3.12-slim' }
    }
    stages {
        stage('Install Tools')  {
            steps {
                sh 'python -m pip install pylint'
            }
        }
        stage('Pylint') {
            steps {
                sh 'PYTHONPATH=pysrc python -m pylint --fail-under=9.8 pysrc'
            }
        }
        stage('Build') {
            steps {
                sh 'python -m build'
            }
        }
        stage('Install') {
            steps {
	        dir("dist") {
                    sh 'python -m pip install helik*.whl'
		}
            }
        }
        stage('ATest') {
            steps {
		sh 'SDL_VIDEODRIVER="dummy" SDL_AUDIODRIVER="disk" python -m helik -q'
            }
        }
        stage('Uninstall') {
            steps {
                ish 'python -m pip uninstall -y helik'
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}

