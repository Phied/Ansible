[[_TOC_]]

# Juniper Roles WIP
### Testing Templates and Variables
- Use this site as long as you're structuring your data in yaml (not json) to test your output of templates.
[Ansible Template Tester](https://ansible.sivel.net/test/)

### Folder structure
- group_vars -  This folder contains variables that contain to various groups contained in the hosts file (/etc/ansible/hosts).  The special one is "all.yml".  This file will match any device since all devices fit the "all group".  The vars should be used for group-wide type settings.  Think tacacs, snmp, etc.

- host_vars -  This folder checks to see if there's a file named for a specific host defined in the /etc/ansible/hosts.  These vars should be used for specific host settings only (ie interface IPs, routes, etc.)

- roles - These folders can be called in the yml file above this directory (by importing role.)  Ansible will automatically look for the folder matching the role you imported.  It will then look for a "templates" and "tasks" directory.  The templates directory are where you will store your jinja templates.  The tasks directory are where you put your tasks you need for that role.  By default ansible looks for a "main.yml" in the tasks directory.

### Juniper

#### Syslog
As long as either the group.yml (that would include the device) or individual host.yml contains the following settings - it will update the syslog server.  We utilize jinja and the "junos_config" to set a line by line update as there is no easy built-in function in Ansible yet.

system:         (required)
  syslog:       (required)
    hosts:      (required - but can have any number of servers below)
      - name: 192.168.1.1       (required)
        port: 1234              (optional - remove line if not using)
      - name: 192.168.3.1       (example of a second server)