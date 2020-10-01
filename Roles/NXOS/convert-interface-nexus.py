---
- name: Gather Interface from Nexus
  hosts: 216.168.47.254
  connection: network_cli
  gather_facts: false
  vars:
    ansible_network_os: nxos_interfaces
  tasks:
  - name: Gather interfaces facts from the device using nxos_interfaces
    cisco.nxos.nxos_interfaces:
      state: gathered