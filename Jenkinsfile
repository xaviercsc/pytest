pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git 'https://github.com/xaviercsc/pytest.git'
            }
        }

        stage('Install Requirements') {
            steps {
                // Install Python requirements
                //sh 'python -m pip install -r requirements.txt'
                echo "Python Installed"
            }
        }

        stage('Run Python Script') {
            steps {
                // Run the Python script and capture the output
                script {
                    def output = sh(script: 'python3 testrun.py', returnStdout: true).trim()
                    echo "Python Script Output:\n${output}"
                }
            }
        }
    }
}
