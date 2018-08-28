node ('jslave') {
    stage ('Checkout') {
        checkout scm
    }

    stage ('Build') {
        sh 'ls -al'
    }

    stage ('Test') {
        sh 'python3 test_primes.py'
    }
}
