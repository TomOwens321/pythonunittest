node ('jslave') {
    stage ('Checkout') {
        checkout scm
    }

    stage ('Build') {
        sh 'echo "No build needed."'
    }

    stage ('Test') {
        sh 'python3 test_primes.py'
    }
}
