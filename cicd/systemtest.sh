#!/bin/bash
jenkinsutils http://192.168.1.1:8080 init
jenkinsutils http://192.168.1.1:8080 plugins download
jenkinsutils http://192.168.1.1:8080 list
jenkinsutils http://192.168.1.1:8080 create config
jenkinsutils http://192.168.1.1:8080 jobstatus

