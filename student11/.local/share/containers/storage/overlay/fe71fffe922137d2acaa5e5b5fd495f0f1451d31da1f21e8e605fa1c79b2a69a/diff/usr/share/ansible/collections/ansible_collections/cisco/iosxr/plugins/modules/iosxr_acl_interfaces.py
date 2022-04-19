#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for iosxr_acl_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: iosxr_acl_interfaces
short_description: ACL interfaces resource module
description:
- This module manages adding and removing Access Control Lists (ACLs) from interfaces
  on devices running IOS-XR software.
version_added: 1.0.0
author: Nilashish Chakraborty (@NilashishC)
options:
  config:
    description: A dictionary of ACL options for interfaces.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name/Identifier for the interface
        type: str
        required: true
      access_groups:
        type: list
        elements: dict
        description:
        - Specifies ACLs attached to the interfaces.
        suboptions:
          afi:
            description:
            - Specifies the AFI for the ACL(s) to be configured on this interface.
            type: str
            choices:
            - ipv4
            - ipv6
            required: true
          acls:
            type: list
            description:
            - Specifies the ACLs for the provided AFI.
            elements: dict
            suboptions:
              name:
                description:
                - Specifies the name of the IPv4/IPv6 ACL for the interface.
                type: str
                required: true
              direction:
                description:
                - Specifies the direction of packets that the ACL will be applied
                  on.
                type: str
                choices:
                - in
                - out
                required: true
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the IOS-XR device
      by executing the command B(show running-config interface).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - parsed
    - rendered
    default: merged

"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:22:32.911 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
# !

- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_1
          direction: in
        - name: acl_2
          direction: out
      - afi: ipv6
        acls:
        - name: acl6_1
          direction: in
        - name: acl6_2
          direction: out

    - name: GigabitEthernet0/0/0/1
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_1
          direction: out
    state: merged

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:27:49.378 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !

# Using merged to update interface ACL configuration

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:27:49.378 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

- name: Update acl_interfaces configuration using merged
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_2
          direction: out
        - name: acl_1
          direction: in
    state: merged

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:27:49.378 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
# !
#

# Using replaced

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !

- name: Replace device configurations of listed interface with provided configurations
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/0
      access_groups:
      - afi: ipv6
        acls:
        - name: acl6_3
          direction: in
    state: replaced

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv6 access-group acl6_3 ingress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

# Using overridden

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

- name: Overridde all interface ACL configuration with provided configuration
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_2
          direction: in
      - afi: ipv6
        acls:
        - name: acl6_3
          direction: out
    state: overridden

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_2 ingress
#  ipv6 access-group acl6_3 egress
# !
#

# Using 'deleted' to delete all ACL attributes of a single interface

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

- name: Delete all ACL attributes of GigabitEthernet0/0/0/1
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
    state: deleted

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
#

# Using 'deleted' to remove all ACLs attached to all the interfaces in the device

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

- name: Delete all ACL interfaces configuration from the device
  cisco.iosxr.iosxr_acl_interfaces:
    state: deleted

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
#

# Using parsed

# parsed.cfg
# ------------
#
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !

# - name: Convert ACL interfaces config to argspec without connecting to the appliance
#   cisco.iosxr.iosxr_acl_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed


# Task Output (redacted)
# -----------------------

# "parsed": [
#        {
#            "name": "MgmtEth0/RP0/CPU0/0"
#        },
#        {
#            "access_groups": [
#                {
#                    "acls": [
#                        {
#                            "direction": "in",
#                            "name": "acl_1"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "acl_2"
#                        }
#                    ],
#                    "afi": "ipv4"
#                },
#                {
#                    "acls": [
#                        {
#                            "direction": "in",
#                            "name": "acl6_1"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "acl6_2"
#                        }
#                    ],
#                    "afi": "ipv6"
#                }
#            ],
#            "name": "GigabitEthernet0/0/0/0"
#        },
#        {
#            "access_groups": [
#                {
#                    "acls": [
#                        {
#                            "direction": "out",
#                            "name": "acl_1"
#                        }
#                    ],
#                    "afi": "ipv4"
#                }
#            ],
#            "name": "GigabitEthernet0/0/0/1"
#        }
#    ]
# }


# Using gathered

- name: Gather ACL interfaces facts using gathered state
  cisco.iosxr.iosxr_acl_interfaces:
    state: gathered


# Task Output (redacted)
# -----------------------
#
# "gathered": [
#   {
#      "name": "MgmtEth0/RP0/CPU0/0"
#   },
#   {
#      "access_groups": [
#          {
#              "acls": [
#                  {
#                      "direction": "in",
#                      "name": "acl_1"
#                  },
#                  {
#                      "direction": "out",
#                      "name": "acl_2"
#                  }
#              ],
#              "afi": "ipv4"
#          }
#      "name": "GigabitEthernet0/0/0/0"
#  },
#  {
#      "access_groups": [
#          {
#              "acls": [
#                  {
#                      "direction": "in",
#                      "name": "acl6_1"
#                  }
#              ],
#              "afi": "ipv6"
#          }
#       "name": "GigabitEthernet0/0/0/1"
#   }
# ]


# Using rendered

- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_1
          direction: in
        - name: acl_2
          direction: out
    state: rendered

# Task Output (redacted)
# -----------------------

# "rendered": [
#     "interface GigabitEthernet0/0/0/0",
#     "ipv4 access-group acl_1 ingress",
#     "ipv4 access-group acl_2 egress"
# ]
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - "interface GigabitEthernet0/0/0/1"
    - "ipv4 access-group acl_1 ingress"
    - "ipv4 access-group acl_2 egress"
    - "ipv6 access-group acl6_1 ingress"
    - "interface GigabitEthernet0/0/0/2"
    - "no ipv4 access-group acl_3 ingress"
    - "ipv4 access-group acl_4 egress"
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.acl_interfaces.acl_interfaces import (
    Acl_interfacesArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.acl_interfaces.acl_interfaces import (
    Acl_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=Acl_interfacesArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    result = Acl_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
