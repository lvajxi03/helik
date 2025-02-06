pipeline {
    agent any
    stages {
        stage('Install Tools')  {
            steps {
                bat """
                python -m pip install pylint
                """
            }
        }
        stage('Pylint') {
            steps {
                bat """
                set PYTHONPATH=pysrc
                python -m pylint --fail-under=9.8 pysrc
                """
            }
        }
        stage('Build') {
            steps {
                bat """
                python -m build
                """
            }
        }
        stage('Install') {
            steps {
	        dir("dist") {
                    bat """
		    python -m pip install helik-0.0.0-py3-none-any.whl
		    """
		}
            }
        }
        stage('ATest') {
            steps {
                bat """
		setSDL_VIDEODRIVER="dummy"
		set SDL_AUDIODRIVER="disk"
                python -m  helik -q
                """
            }
        }
        stage('Uninstall') {
            steps {
                bat """
                python -m pip uninstall helik
                """
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}

