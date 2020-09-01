In order to get Junos Netconf to work may need to check:
- connection is set to netconf (sometimes need local)
- may need to set your python interpreter (/usr/bin/python3) manually
- junos.eznc, ncclient, lxml and possible other dependencies installed via pip

To create common directory structure for new role:
ansible-galaxy init <role>

At the end of a Project update, Tower searches for a file called requirements.yml in the roles directory, located at <project-top-level-directory>/roles/requirements.yml. If this file is found, the following command automatically runs:

ansible-galaxy install -r roles/requirements.yml -p <project-specific cache location>/requirements_roles -vvv