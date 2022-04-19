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
The module file for junos_lacp_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_lacp_interfaces
short_description: LACP interfaces resource module
description:
- This module manages Link Aggregation Control Protocol (LACP) attributes of interfaces
  on Juniper JUNOS devices.
version_added: 1.0.0
author: Ganesh Nalawade (@ganeshrn)
options:
  config:
    description: The list of dictionaries of LACP interfaces options.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name Identifier of the interface or link aggregation group.
        type: str
      period:
        description:
        - Timer interval for periodic transmission of LACP packets. If the value is
          set to C(fast) the packets are received every second and if the value is
          C(slow) the packets are received every 30 seconds. This value is applicable
          for aggregate interface only.
        type: str
        choices:
        - fast
        - slow
      sync_reset:
        description:
        - The argument notifies minimum-link failure out of sync to peer. If the value
          is C(disable) it disables minimum-link failure handling at LACP level and
          if value is C(enable) it enables minimum-link failure handling at LACP level.
          This value is applicable for aggregate interface only.
        type: str
        choices:
        - disable
        - enable
      force_up:
        description:
        - This is a boolean argument to control if the port should be up in absence
          of received link Aggregation Control Protocol Data Unit (LACPDUS). This
          value is applicable for member interfaces only.
        type: bool
      port_priority:
        description:
        - Priority of the member port. This value is applicable for member interfaces
          only.
        - Refer to vendor documentation for valid values.
        type: int
      system:
        description:
        - This dict object contains configurable options related to LACP system parameters
          for the link aggregation group. This value is applicable for aggregate interface
          only.
        type: dict
        suboptions:
          priority:
            description:
            - Specifies the system priority to use in LACP negotiations for the bundle.
            - Refer to vendor documentation for valid values.
            type: int
          mac:
            description:
            - Specifies the system ID to use in LACP negotiations for the bundle,
              encoded as a MAC address.
            type: dict
            suboptions:
              address:
                description:
                - The system ID to use in LACP negotiations.
                type: str
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show interface).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state of the configuration after module completion.
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
# user@junos01# show interfaces
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae4;
#     }
# }
# ge-0/0/3 {
#    ether-options {
#         802.3ad ae0;
#     }
# }
# ae0 {
#     description "lag interface merged";
#     aggregated-ether-options {
#         lacp {
#             passive;
#         }
#     }
# }
# ae4 {
#     description "test aggregate interface";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             link-protection;
#         }
#     }
# }

- name: Merge provided configuration with device configuration
  junipernetworks.junos.junos_lacp_interfaces:
    config:
    - name: ae0
      period: fast
      sync_reset: enable
      system:
        priority: 100
        mac:
          address: 00:00:00:00:00:02
    - name: ge-0/0/3
      port_priority: 100
      force_up: true
    state: merged

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae4;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 force-up;
#                 port-priority 100;
#             }
#             ae0;
#         }
#     }
# }
# ae0 {
#     description "lag interface merged";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             periodic fast;
#             sync-reset enable;
#             system-priority 100;
#             system-id 00:00:00:00:00:02;
#         }
#     }
# }
# ae4 {
#     description "test aggregate interface";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             link-protection;
#         }
#     }
# }

# Using replaced
# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae4;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 force-up;
#                 port-priority 100;
#             }
#             ae0;
#         }
#     }
# }
# ae0 {
#     description "lag interface merged";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             periodic fast;
#             sync-reset enable;
#             system-priority 100;
#             system-id 00:00:00:00:00:02;
#         }
#     }
# }
# ae4 {
#     description "test aggregate interface";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             link-protection;
#         }
#     }
# }

- name: Replace device LACP interfaces configuration with provided configuration
  junipernetworks.junos.junos_lacp_interfaces:
    config:
    - name: ae0
      period: slow
    state: replaced

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae4;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 force-up;
#                 port-priority 100;
#             }
#             ae0;
#         }
#     }
# }
# ae0 {
#     description "lag interface merged";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             periodic slow;
#         }
#     }
# }
# ae4 {
#     description "test aggregate interface";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             link-protection;
#         }
#     }
# }

# Using overridden
# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae4;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 force-up;
#                 port-priority 100;
#             }
#             ae0;
#         }
#     }
# }
# ae0 {
#     description "lag interface merged";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             periodic slow;
#         }
#     }
# }
# ae4 {
#     description "test aggregate interface";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             link-protection;
#         }
#     }
# }

- name: Overrides all device LACP interfaces configuration with provided configuration
  junipernetworks.junos.junos_lacp_interfaces:
    config:
    - name: ae0
      system:
        priority: 300
        mac:
          address: 00:00:00:00:00:03
    - name: ge-0/0/2
      port_priority: 200
      force_up: false
    state: overridden

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/2 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 port-priority 200;
#             }
#             ae4;
#         }
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 force-up;
#                 port-priority 100;
#             }
#             ae0;
#         }
#     }
# }
# ae0 {
#     description "lag interface merged";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             system-priority 300;
#             system-id 00:00:00:00:00:03;
#         }
#     }
# }
# ae4 {
#     description "test aggregate interface";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             link-protection;
#         }
#     }
# }

# Using deleted
# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/2 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 port-priority 200;
#             }
#             ae4;
#         }
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 force-up;
#                 port-priority 100;
#             }
#             ae0;
#         }
#     }
# }
# ae0 {
#     description "lag interface merged";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             system-priority 300;
#             system-id 00:00:00:00:00:03;
#         }
#     }
# }
# ae4 {
#     description "test aggregate interface";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             link-protection;
#         }
#     }
# }

- name: "Delete LACP interfaces attributes of given interfaces (Note: This won't delete the interface itself)"
  junipernetworks.junos.junos_lacp_interfaces:
    config:
    - name: ae0
    - name: ge-0/0/3
    - name: ge-0/0/2
    state: deleted

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae4;
#     }
# }
# ge-0/0/3 {
#    ether-options {
#         802.3ad ae0;
#     }
# }
# ae0 {
#     description "lag interface merged";
#     aggregated-ether-options {
#         lacp {
#             passive;
#         }
#     }
# }
# ae4 {
#     description "test aggregate interface";
#     aggregated-ether-options {
#         lacp {
#             passive;
#             link-protection;
#         }
#     }
# }
# Using gathered
# Before state:
# ------------
#
# user@junos01# show interfaces
# ansible@cm123456tr21# show interfaces
# ge-0/0/1 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 force-up;
#                 port-priority 100;
#             }
#             ae1;
#         }
#     }
# }
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad ae2;
#     }
# }
# ge-0/0/4 {
#     ether-options {
#         802.3ad ae2;
#     }
# }
# ge-1/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.1/24;
#             address 10.200.16.20/24;
#         }
#         family inet6;
#     }
# }
# ge-2/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.2/24;
#             address 10.200.16.21/24;
#         }
#         family inet6;
#     }
# }
# ge-3/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.3/24;
#             address 10.200.16.22/24;
#         }
#         family inet6;
#     }
# }
# ae1 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         lacp {
#             periodic fast;
#             sync-reset enable;
#             system-priority 100;
#             system-id 00:00:00:00:00:02;
#         }
#     }
# }
# ae2 {
#     description "Configured by Ansible";
# }
# em1 {
#     description TEST;
# }
# fxp0 {
#     description ANSIBLE;
#     speed 1g;
#     link-mode automatic;
#     unit 0 {
#         family inet {
#             address 10.8.38.38/24;
#         }
#     }
# }
- name: Gather junos lacp interfaces as in given arguments
  junipernetworks.junos.junos_lacp_interfaces:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "force_up": true,
#             "name": "ge-0/0/1",
#             "port_priority": 100
#         },
#         {
#             "name": "ae1",
#             "period": "fast",
#             "sync_reset": "enable",
#             "system": {
#                 "mac": {
#                     "address": "00:00:00:00:00:02"
#                 },
#                 "priority": 100
#             }
#         }
#     ]
# After state:
# ------------
#
# ansible@cm123456tr21# show interfaces
# ge-0/0/1 {
#     ether-options {
#         802.3ad {
#             lacp {
#                 force-up;
#                 port-priority 100;
#             }
#             ae1;
#         }
#     }
# }
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad ae2;
#     }
# }
# ge-0/0/4 {
#     ether-options {
#         802.3ad ae2;
#     }
# }
# ge-1/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.1/24;
#             address 10.200.16.20/24;
#         }
#         family inet6;
#     }
# }
# ge-2/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.2/24;
#             address 10.200.16.21/24;
#         }
#         family inet6;
#     }
# }
# ge-3/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.3/24;
#             address 10.200.16.22/24;
#         }
#         family inet6;
#     }
# }
# ae1 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         lacp {
#             periodic fast;
#             sync-reset enable;
#             system-priority 100;
#             system-id 00:00:00:00:00:02;
#         }
#     }
# }
# ae2 {
#     description "Configured by Ansible";
# }
# em1 {
#     description TEST;
# }
# fxp0 {
#     description ANSIBLE;
#     speed 1g;
#     link-mode automatic;
#     unit 0 {
#         family inet {
#             address 10.8.38.38/24;
#         }
#     }
# }
# Using parsed
# parsed.cfg
# ------------
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
# <interfaces>
#         <interface>
#             <name>ge-0/0/1</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <lacp>
#                         <force-up/>
#                         <port-priority>100</port-priority>
#                     </lacp>
#                     <bundle>ae1</bundle>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/2</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae1</bundle>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/3</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae2</bundle>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/4</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae2</bundle>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-1/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.1/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.20/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ge-2/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.2/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.21/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ge-3/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.3/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.22/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ae1</name>
#             <description>Configured by Ansible</description>
#             <aggregated-ether-options>
#                 <lacp>
#                     <periodic>fast</periodic>
#                     <sync-reset>enable</sync-reset>
#                     <system-priority>100</system-priority>
#                     <system-id>00:00:00:00:00:02</system-id>
#                 </lacp>
#             </aggregated-ether-options>
#         </interface>
#         <interface>
#             <name>ae2</name>
#             <description>Configured by Ansible</description>
#         </interface>
#         <interface>
#             <name>em1</name>
#             <description>TEST</description>
#         </interface>
#         <interface>
#             <name>fxp0</name>
#             <description>ANSIBLE</description>
#             <speed>1g</speed>
#             <link-mode>automatic</link-mode>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>10.8.38.38/24</name>
#                         </address>
#                     </inet>
#                 </family>
#             </unit>
#         </interface>
#     </interfaces>
#     </configuration>
# </rpc-reply>
# - name: Convert interfaces config to argspec without connecting to the appliance
#   junipernetworks.junos.junos_lacp_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#         {
#             "force_up": true,
#             "name": "ge-0/0/1",
#             "port_priority": 100
#         },
#         {
#             "name": "ae1",
#             "period": "fast",
#             "sync_reset": "enable",
#             "system": {
#                 "mac": {
#                     "address": "00:00:00:00:00:02"
#                 },
#                 "priority": 100
#             }
#         }
#     ]
# Using rendered
- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_lacp_interfaces:
    config:
     - name: ae1
       period: fast
       sync_reset: enable
       system:
         priority: 100
         mac:
           address: 00:00:00:00:00:02

     - name: ge-0/0/1
       port_priority: 100
       force_up: true
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": "<nc:interfaces
#     xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#     <nc:interface>
#         <nc:name>ae1</nc:name>
#         <nc:aggregated-ether-options>
#             <nc:lacp>
#                 <nc:periodic>fast</nc:periodic>
#                 <nc:sync-reset>enable</nc:sync-reset>
#                 <nc:system-id>00:00:00:00:00:02</nc:system-id>
#                 <nc:system-priority>100</nc:system-priority>
#             </nc:lacp>
#         </nc:aggregated-ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/1</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:lacp>
#                     <nc:port-priority>100</nc:port-priority>
#                     <nc:force-up/>
#                 </nc:lacp>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
# </nc:interfaces>"

"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['<nc:interfaces
    xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
    <nc:interface>
        <nc:name>ae1</nc:name>
        <nc:aggregated-ether-options>
            <nc:lacp>
                <nc:periodic>fast</nc:periodic>
                <nc:sync-reset>enable</nc:sync-reset>
                <nc:system-id>00:00:00:00:00:02</nc:system-id>
                <nc:system-priority>100</nc:system-priority>
            </nc:lacp>
        </nc:aggregated-ether-options>
    </nc:interface>
    <nc:interface>
        <nc:name>ge-0/0/1</nc:name>
        <nc:ether-options>
            <nc:ieee-802.3ad>
                <nc:lacp>
                    <nc:port-priority>100</nc:port-priority>
                    <nc:force-up/>
                </nc:lacp>
            </nc:ieee-802.3ad>
        </nc:ether-options>
    </nc:interface>
</nc:interfaces>', 'xml 2', 'xml 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.lacp_interfaces.lacp_interfaces import (
    Lacp_interfacesArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.lacp_interfaces.lacp_interfaces import (
    Lacp_interfaces,
)


def main():
    """
    Main entry point for module execution
    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]

    module = AnsibleModule(
        argument_spec=Lacp_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    result = Lacp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
