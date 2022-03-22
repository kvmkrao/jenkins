pipeline {
    agent any

    stages {
        stage('Pull') {
            steps {
                echo 'git'
                git 'https://github.com/kvmkrao/jenkins.git' 
            }
        }
        stage('Configure') {
            steps {
                dir('build') {
                    echo 'configure'
                    //'cmake 'InSearchPath' ''
                }
            }
        }
    
        stage('Build') {
            steps {
                echo 'build'
                //sh 'cmake --build .' 
            }
        }

        stage('Test') {
            steps {
                echo 'Test'
                //ctest 'InSearchPath' */
            }
        }

        stage('Build image') {
            steps{
                script {
                echo 'docker image'
                /* dockerImage = docker.build dockerimagename */
                }   
            }
        }

        stage('Pushing Image') {
            environment {
                registryCredential = 'dockerhublogin'
            }
            steps{
                script {
                echo 'registry'
            /* docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
              dockerImage.push("latest")  */
                }
            }
        }
  
        stage('Deploying App to Kubernetes') {
            steps {
                script {
                    echo 'deploy'    
                    /* kubernetesDeploy(configs: "deploymentservice.yml", kubeconfigId: "kubernetes") */
                }
            }  
        }
    
    }
}
