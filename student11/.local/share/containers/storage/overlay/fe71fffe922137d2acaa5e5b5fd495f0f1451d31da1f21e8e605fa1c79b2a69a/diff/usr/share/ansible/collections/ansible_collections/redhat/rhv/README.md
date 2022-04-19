[![Build Status](https://jenkins.ovirt.org/job/oVirt_ovirt-ansible-collection_standard-check-pr/badge/icon)](https://jenkins.ovirt.org/job/oVirt_ovirt-ansible-collection_standard-check-pr/)
[![Build Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://docs.ansible.com/ansible/2.10/collections/ovirt/ovirt/index.html)

oVirt Ansible Collection
====================================

The `redhat.rhv` manages all oVirt Ansible modules.

The pypi installation is no longer supported if you want
to install all dependencies do it manually or install the
collection from RPM and it will be done automatically.

Note
----
Please note that when installing this collection from Ansible Galaxy you are instructed to run following command:

```bash
$ ansible-galaxy collection install redhat.rhv
```

Requirements
------------

 * Ansible version 2.9.11 or higher
 * Python SDK version 4.4 or higher
 * Python netaddr library on the ansible controller node

Content of the collection
----------------

* modules:
  * ovirt_* - Modules to manage objects in rhv Engine
  * ovirt_*_info - Modules to gather information about objects in rhv Engine
* roles:
  * cluster_upgrade
  * engine_setup
  * hosted_engine_setup
  * image_template
  * infra
  * manageiq
  * repositories
  * shutdown_env
  * vm_infra
  * disaster_recovery
* inventory plugin


Example Playbook
----------------

```yaml
---
- name: rhv ansible collection
  hosts: localhost
  connection: local
  vars_files:
    # Contains encrypted `engine_password` varibale using ansible-vault
    - passwords.yml
  tasks:
    - block:
        # The use of redhat.rhv before ovirt_auth is to check if the collection is correctly loaded
        - name: Obtain SSO token with using username/password credentials
          redhat.rhv.ovirt_auth:
            url: https://ovirt.example.com/ovirt-engine/api
            username: admin@internal
            ca_file: ca.pem
            password: "{{ ovirt_password }}"

        # Previous task generated I(ovirt_auth) fact, which you can later use
        # in different modules as follows:
        - ovirt_vm:
            auth: "{{ ovirt_auth }}"
            state: absent
            name: myvm

      always:
        - name: Always revoke the SSO token
          ovirt_auth:
            state: absent
            ovirt_auth: "{{ ovirt_auth }}"
  collections:
    - redhat.rhv
```

Licenses
-------

- Apache License 2.0
- GNU General Public License 3.0