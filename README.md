# jenkinsutils
This setup is not meant for production.  It is only for learning purposes.

## Initialization
1. Install Docker and docker-compose
2. Change to the cicd directory and run docker-compose up -d
3. Setup Jenkins
  1. cat cicd/jenkins_home/secrets/initialAdminPassword
  2. Navigate to 192.168.1.1 and put in that password
  3. Install recommended plugins
  4. Continue as admin (no new user)
  5. Manage Jenkins -> Configure Global Security
    1. Disable Enable security
    2. Disable Prevent Cross Site Request Forgery exploits
    3. Save
  6. Manage Jenkins -> Manage Nodes -> New Node
    1. Build Node, Permanent Agent
    2. Setup:
       1. Number of Executors: 2
       2. Remote root directory: /root
       3. Labels: Build Node
       4. Launch method: SSH
         1. Host: 192.168.1.2
         2. Add Jenkins credential: root/root (and use it)
         3. Non verifying Verification Strategy
         4. Save
         5. Make sure the node connects.
  7. Repeat steps 1-5 for the system test container (docker-compose -f systemtest.yml up)
4. Setup GitLab
  1. Navigate to 192.168.1.3
  2. Put in a password and change password
  3. Log in as root and the password you set
  4. Add an SSH key for root
  5. Create a jenkinsutils project
    1. Public access
    2. Located at http://192.168.1.3/root/jenkinsutils

## Usage
After installing the jenkinsutils package, the following commands are available:

* jenkinsutils [Jenkins URL:port] plugins-download [config file]
* jenkinsutils [Jenkins URL:port] plugins-list
* jenkinsutils [Jenkins URL:port] job-create [config file]
* jenkinsutils [Jenkins URL:port] job-status

See jenkinsutils --help for more information about each command.

## Testing
Change to the cicd directory.  Then...

* **jenkinsutils installation**
  * docker-compose -f unittest.yml build OR
  * pip install --force -e jenkinsutils from the directory above setup.py
* **jenkinsutils unittesting**
  * docker-compose -f unittest.yml run --rm unittest
  * From the top directory, run nose2
* **jenkinsutils system testing**
  * docker-compose -f systemtest.yml up --abort-on-container-exit
  * No manual version of this
