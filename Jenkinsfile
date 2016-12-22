node('master') {
  stage('Checkout') {
    deleteDir()
    git credentialsId: '603920ee-6645-4d0f-8af3-c8687a5d65f5', url: 'git@github.com:beeva-AlejandroHernandez/course-cicd.git'
  }

   stage('Test') {
    sh './simplehttpserver/tests/unittests.sh ./simplehttpserver/'
  }

}
