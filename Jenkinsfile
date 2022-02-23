node{
    agent{
        label "node"
    }
    stages{
        stage("Build Stage"){
            steps{
                echo "========executing A========"
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Test Stage"){
            steps{
                echo "========executing B========"
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========B executed successfully========"
                }
                failure{
                    echo "========B execution failed========"
                }
            }
        }

    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
            stage("Deploy Stage"){
            steps{
                echo "========executing C========"
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========C executed successfully========"
                }
                failure{
                    echo "========C execution failed========"
                }
            }
        }
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}