pipeline {

agent any

tools {
        maven 'maven'

   }
   
stages {

        stage('checking maven installation') {
   
             steps {
                    sh 'mvn -v'
             }
        }

        stage ('building java project') {
        
            steps {
                    sh 'cd jspapp-master ; mvn clean package'
                     
            }
        }    
        stage( 'deploy war file in the local docker engine'){
                steps {
                        sh 'docker-compose down : docker-compose up -d'
                        
                      }
        }
                        
  }



}
