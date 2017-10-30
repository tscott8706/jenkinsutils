#!/bin/bash
jenkinsutils http://192.168.1.1:8080 plugins-download --config config
jenkinsutils http://192.168.1.1:8080 plugins-list
jenkinsutils http://192.168.1.1:8080 job-create --config config
jenkinsutils http://192.168.1.1:8080 job-status

