Red Hat Enterprise Linux System Roles Ansible Collection
=====================================

Red Hat Enterprise Linux System Roles is a set of roles for managing Red Hat Enterprise Linux system components.

## Dependencies

The following dependency is required for the Ansible Controller:
* jmespath

## Installation

There are currently two ways to use the Red Hat Enterprise Linux System Roles Collection in your setup.

### Installation from Automation Hub

You can install the collection from Automation Hub by running:
```
ansible-galaxy collection install redhat.rhel_system_roles
```

After the installation, the roles are available as `redhat.rhel_system_roles.<role_name>`.

Please see the [Using Ansible collections documentation](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for further details.

### Installation via RPM

You can install the collection with the software package management tool `dnf` by running:
```
dnf install rhel-system-roles
```

## Documentation
The official RHEL System Roles documentation can be found in the [Product Documentation section of the Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/administration_and_configuration_tasks_using_system_roles_in_rhel/index).

## Support

### Supported Ansible Versions

The supported Ansible versions are aligned with currently maintained Ansible versions that support Collections (Ansible 2.9 and later). You can find the list of maintained Ansible versions [here](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#release-status).

### Modules and Plugins

The modules and other plugins in this collection are private, used only internally to the collection, unless otherwise noted.


### Supported Roles

<!--ts-->
  * [postfix](roles/postfix/README.md)
  * [selinux](roles/selinux/README.md)
  * [timesync](roles/timesync/README.md)
  * [kdump](roles/kdump/README.md)
  * [network](roles/network/README.md)
  * [storage](roles/storage/README.md)
  * [metrics](roles/metrics/README.md)
  * [tlog](roles/tlog/README.md)
  * [kernel_settings](roles/kernel_settings/README.md)
  * [logging](roles/logging/README.md)
  * [nbde_server](roles/nbde_server/README.md)
  * [nbde_client](roles/nbde_client/README.md)
  * [certificate](roles/certificate/README.md)
  * [crypto_policies](roles/crypto_policies/README.md)
  * [sshd](roles/sshd/README.md)
  * [ssh](roles/ssh/README.md)
  * [ha_cluster](roles/ha_cluster/README.md)
<!--te-->

### Private Roles

<!--ts-->
  * [private_metrics_subrole_redis](roles/private_metrics_subrole_redis/README.md)
  * [private_metrics_subrole_pcp](roles/private_metrics_subrole_pcp/README.md)
  * [private_metrics_subrole_mssql](roles/private_metrics_subrole_mssql/README.md)
  * [private_metrics_subrole_grafana](roles/private_metrics_subrole_grafana/README.md)
  * [private_metrics_subrole_elasticsearch](roles/private_metrics_subrole_elasticsearch/README.md)
  * [private_metrics_subrole_bpftrace](roles/private_metrics_subrole_bpftrace/README.md)
  * [private_logging_subrole_rsyslog](roles/private_logging_subrole_rsyslog/README.md)
<!--te-->
