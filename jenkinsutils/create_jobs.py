import jenkinsapi
import json

def create_jobs(srv, config_filepath):
    for job_name, repo_and_jenkinsfile in _parse_config(config_filepath).items():
        srv.create_job(job_name, _get_job_config(repo_and_jenkinsfile))

def _parse_config(config_filepath):
    with open(config_filepath, "r") as config_file:
        return json.load(config_file)

def _get_job_config(repo_and_jenkinsfile):
    repo, jenkinsfile = repo_and_jenkinsfile
    return """<?xml version='1.0' encoding='UTF-8'?>
<flow-definition plugin="workflow-job@2.15">
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties>
    <org.jenkinsci.plugins.workflow.job.properties.PipelineTriggersJobProperty>
      <triggers/>
    </org.jenkinsci.plugins.workflow.job.properties.PipelineTriggersJobProperty>
  </properties>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps@2.41">
    <scm class="hudson.plugins.git.GitSCM" plugin="git@3.6.3">
      <configVersion>2</configVersion>
      <userRemoteConfigs>
        <hudson.plugins.git.UserRemoteConfig>
          <url>{repo}</url>
        </hudson.plugins.git.UserRemoteConfig>
      </userRemoteConfigs>
      <branches>
        <hudson.plugins.git.BranchSpec>
          <name>*/master</name>
        </hudson.plugins.git.BranchSpec>
      </branches>
      <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
      <submoduleCfg class="list"/>
      <extensions/>
    </scm>
    <scriptPath>{jenkinsfile}</scriptPath>
    <lightweight>true</lightweight>
  </definition>
  <triggers/>
  <disabled>false</disabled>
</flow-definition>
""".format(repo=repo, jenkinsfile=jenkinsfile)
