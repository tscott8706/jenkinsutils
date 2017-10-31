#!/bin/bash
#jenkinsutils http://192.168.2.1:8080 plugins-download --config config
#jenkinsutils http://192.168.2.1:8080 plugins-list
sleep 60
rm -rf jenkins_home_test/jobs/*
jenkinsutils http://192.168.2.1:8080 job-create --config config
#jenkinsutils http://192.168.2.1:8080 job-status

