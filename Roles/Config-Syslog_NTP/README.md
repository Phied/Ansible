### This role is to be used to configure syslog servers on network devices.  


1.  Be sure to set the syslog settings in the group_vars. (only name is required)
2.  Modify hosts in the syslog-play.yml to select desired hosts (or specify via cli) and run - can use "all" if desired in this file.
3.  ansible-playbook ./syslog-play.yaml <any other flags you wish>

If you get an error about module missing - 
- ansible-galaxy collection install cisco.ios
- ansible-galaxy collection install cisco.iosxr