#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#jenkinsutils http://192.168.2.1:8080 plugins-download --config config
#jenkinsutils http://192.168.2.1:8080 plugins-list
rm -rf $DIR/jenkins_home_test/jobs/*
jenkinsutils http://192.168.2.1:8080 job-create --config $DIR/systemtest_job_config.json
#jenkinsutils http://192.168.2.1:8080 job-status

