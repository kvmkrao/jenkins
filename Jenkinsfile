pipeline {
    agent any

    stages {

    stage('Checkout source'){
      steps {
             git 'https://github.com/kvmkrao/jenkins.git'
      }
      }

    stage('Configure') {
      steps {
          sh 'cmake .'
      }
    }
     stage('Build') {
        steps {
          sh 'cmake --build .'
        }
     }

     stage('Test') {
            steps {
                ctest 'InSearchPath'
            }
     }

     stage('Build image') {
       steps{
         script {
           dockerImage = docker.build dockerimagename
         }
       }
     }

    stage('Pushing Image') {
      environment {
               registryCredential = 'dockerhublogin'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            dockerImage.push("latest")
          }
        }
      }
    }

    stage('Deploy') {
            when {
                environment name: 'DEPLOY', value: 'true'
            }
            steps {
                sh label: '', returnStatus: true, script: '''cp jenkinsexample ~
                cp test/testPro ~'''
            }
        }
    }
}
