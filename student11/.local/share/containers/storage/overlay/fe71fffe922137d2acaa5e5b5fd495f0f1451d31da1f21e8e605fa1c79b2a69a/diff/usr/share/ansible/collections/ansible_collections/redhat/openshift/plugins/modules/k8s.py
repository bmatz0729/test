#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Chris Houseknecht <@chouseknecht>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = '''
author:
- Chris Houseknecht (@chouseknecht)
- Fabian von Feilitzsch (@fabianvf)
description:
- Use the Kubernetes Python client to perform CRUD operations on K8s objects.
- Pass the object definition from a source file or inline. See examples for reading
  files and using Jinja templates or vault-encrypted files.
- Access to the full range of K8s APIs.
- Use the M(kubernetes.core.k8s_info) module to obtain a list of items about an object
  of type C(kind).
- Authenticate using either a config file, certificates, password or token.
- Supports check mode.
- Optimized for OKD/OpenShift Kubernetes flavors.
module: k8s
notes:
- To avoid SSL certificate validation errors when C(validate_certs) is I(True), the
  full certificate chain for the API server must be provided via C(ca_cert) or in
  the kubeconfig file.
options:
  api_key:
    description:
    - Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY
      environment variable.
    type: str
  api_version:
    aliases:
    - api
    - version
    default: v1
    description:
    - Use to specify the API version.
    - Use to create, delete, or discover an object without providing a full resource
      definition.
    - Use in conjunction with I(kind), I(name), and I(namespace) to identify a specific
      object.
    - If I(resource definition) is provided, the I(apiVersion) value from the I(resource_definition)
      will override this option.
    type: str
  append_hash:
    default: false
    description:
    - Whether to append a hash to a resource name for immutability purposes
    - Applies only to ConfigMap and Secret resources
    - The parameter will be silently ignored for other resource kinds
    - The full definition of an object is needed to generate the hash - this means
      that deleting an object created with append_hash will only work if the same
      object is passed with state=absent (alternatively, just use state=absent with
      the name including the generated hash and append_hash=no)
    type: bool
  apply:
    default: false
    description:
    - C(apply) compares the desired resource definition with the previously supplied
      resource definition, ignoring properties that are automatically generated
    - C(apply) works better with Services than 'force=yes'
    - mutually exclusive with C(merge_type)
    type: bool
  ca_cert:
    aliases:
    - ssl_ca_cert
    description:
    - Path to a CA certificate used to authenticate with the API. The full certificate
      chain must be provided to avoid certificate validation errors. Can also be specified
      via K8S_AUTH_SSL_CA_CERT environment variable.
    type: path
  client_cert:
    aliases:
    - cert_file
    description:
    - Path to a certificate used to authenticate with the API. Can also be specified
      via K8S_AUTH_CERT_FILE environment variable.
    type: path
  client_key:
    aliases:
    - key_file
    description:
    - Path to a key file used to authenticate with the API. Can also be specified
      via K8S_AUTH_KEY_FILE environment variable.
    type: path
  context:
    description:
    - The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT
      environment variable.
    type: str
  continue_on_error:
    default: false
    description:
    - Whether to continue on creation/deletion errors when multiple resources are
      defined.
    - This has no effect on the validation step which is controlled by the C(validate.fail_on_error)
      parameter.
    type: bool
    version_added: 2.0.0
    version_added_collection: redhat.openshift
  delete_options:
    description:
    - Configure behavior when deleting an object.
    - Only used when I(state=absent).
    suboptions:
      gracePeriodSeconds:
        description:
        - Specify how many seconds to wait before forcefully terminating.
        - Only implemented for Pod resources.
        - If not specified, the default grace period for the object type will be used.
        type: int
      preconditions:
        description:
        - Specify condition that must be met for delete to proceed.
        suboptions:
          resourceVersion:
            description:
            - Specify the resource version of the target object.
            type: str
          uid:
            description:
            - Specify the UID of the target object.
            type: str
        type: dict
      propagationPolicy:
        choices:
        - Foreground
        - Background
        - Orphan
        description:
        - Use to control how dependent objects are deleted.
        - If not specified, the default policy for the object type will be used. This
          may vary across object types.
        type: str
    type: dict
    version_added: 1.2.0
    version_added_collection: kubernetes.core
  force:
    default: false
    description:
    - If set to C(yes), and I(state) is C(present), an existing object will be replaced.
    type: bool
  host:
    description:
    - Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST
      environment variable.
    type: str
  kind:
    description:
    - Use to specify an object model.
    - Use to create, delete, or discover an object without providing a full resource
      definition.
    - Use in conjunction with I(api_version), I(name), and I(namespace) to identify
      a specific object.
    - If I(resource definition) is provided, the I(kind) value from the I(resource_definition)
      will override this option.
    type: str
  kubeconfig:
    description:
    - Path to an existing Kubernetes config file. If not provided, and no other connection
      options are provided, the Kubernetes client will attempt to load the default
      configuration file from I(~/.kube/config). Can also be specified via K8S_AUTH_KUBECONFIG
      environment variable.
    type: path
  merge_type:
    choices:
    - json
    - merge
    - strategic-merge
    description:
    - Whether to override the default patch merge approach with a specific type. By
      default, the strategic merge will typically be used.
    - For example, Custom Resource Definitions typically aren't updatable by the usual
      strategic merge. You may want to use C(merge) if you see "strategic merge patch
      format is not supported"
    - See U(https://kubernetes.io/docs/tasks/run-application/update-api-object-kubectl-patch/#use-a-json-merge-patch-to-update-a-deployment)
    - If more than one merge_type is given, the merge_types will be tried in order
    - Defaults to C(['strategic-merge', 'merge']), which is ideal for using the same
      parameters on resource kinds that combine Custom Resources and built-in resources.
    - mutually exclusive with C(apply)
    - I(merge_type=json) is deprecated and will be removed in version 3.0.0. Please
      use M(kubernetes.core.k8s_json_patch) instead.
    elements: str
    type: list
  name:
    description:
    - Use to specify an object name.
    - Use to create, delete, or discover an object without providing a full resource
      definition.
    - Use in conjunction with I(api_version), I(kind) and I(namespace) to identify
      a specific object.
    - If I(resource definition) is provided, the I(metadata.name) value from the I(resource_definition)
      will override this option.
    type: str
  namespace:
    description:
    - Use to specify an object namespace.
    - Useful when creating, deleting, or discovering an object without providing a
      full resource definition.
    - Use in conjunction with I(api_version), I(kind), and I(name) to identify a specific
      object.
    - If I(resource definition) is provided, the I(metadata.namespace) value from
      the I(resource_definition) will override this option.
    type: str
  password:
    description:
    - Provide a password for authenticating with the API. Can also be specified via
      K8S_AUTH_PASSWORD environment variable.
    - Please read the description of the C(username) option for a discussion of when
      this option is applicable.
    type: str
  persist_config:
    description:
    - Whether or not to save the kube config refresh tokens. Can also be specified
      via K8S_AUTH_PERSIST_CONFIG environment variable.
    - When the k8s context is using a user credentials with refresh tokens (like oidc
      or gke/gcloud auth), the token is refreshed by the k8s python client library
      but not saved by default. So the old refresh token can expire and the next auth
      might fail. Setting this flag to true will tell the k8s python client to save
      the new refresh token to the kube config file.
    - Default to false.
    - Please note that the current version of the k8s python client library does not
      support setting this flag to True yet.
    - 'The fix for this k8s python library is here: https://github.com/kubernetes-client/python-base/pull/169'
    type: bool
  proxy:
    description:
    - The URL of an HTTP proxy to use for the connection. Can also be specified via
      K8S_AUTH_PROXY environment variable.
    - Please note that this module does not pick up typical proxy settings from the
      environment (e.g. HTTP_PROXY).
    type: str
  proxy_headers:
    description:
    - The Header used for the HTTP proxy.
    - Documentation can be found here U(https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight=proxy_headers#urllib3.util.make_headers).
    suboptions:
      basic_auth:
        description:
        - Colon-separated username:password for basic authentication header.
        - Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment.
        type: str
      proxy_basic_auth:
        description:
        - Colon-separated username:password for proxy basic authentication header.
        - Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment.
        type: str
      user_agent:
        description:
        - String representing the user-agent you want, such as foo/1.0.
        - Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment.
        type: str
    type: dict
    version_added: 2.0.0
    version_added_collection: kubernetes.core
  resource_definition:
    aliases:
    - definition
    - inline
    description:
    - Provide a valid YAML definition (either as a string, list, or dict) for an object
      when creating or updating.
    - 'NOTE: I(kind), I(api_version), I(name), and I(namespace) will be overwritten
      by corresponding values found in the provided I(resource_definition).'
  src:
    description:
    - 'Provide a path to a file containing a valid YAML definition of an object or
      objects to be created or updated. Mutually exclusive with I(resource_definition).
      NOTE: I(kind), I(api_version), I(name), and I(namespace) will be overwritten
      by corresponding values found in the configuration read in from the I(src) file.'
    - Reads from the local file system. To read from the Ansible controller's file
      system, including vaulted files, use the file lookup plugin or template lookup
      plugin, combined with the from_yaml filter, and pass the result to I(resource_definition).
      See Examples below.
    - Mutually exclusive with I(template) in case of M(k8s) module.
    type: path
  state:
    choices:
    - absent
    - present
    - patched
    default: present
    description:
    - Determines if an object should be created, patched, or deleted. When set to
      C(present), an object will be created, if it does not already exist. If set
      to C(absent), an existing object will be deleted. If set to C(present), an existing
      object will be patched, if its attributes differ from those specified using
      I(resource_definition) or I(src).
    - C(patched) state is an existing resource that has a given patch applied. If
      the resource doesn't exist, silently skip it (do not raise an error).
    type: str
  template:
    description:
    - Provide a valid YAML template definition file for an object when creating or
      updating.
    - Value can be provided as string or dictionary.
    - Mutually exclusive with C(src) and C(resource_definition).
    - Template files needs to be present on the Ansible Controller's file system.
    - Additional parameters can be specified using dictionary.
    - 'Valid additional parameters - '
    - 'C(newline_sequence) (str): Specify the newline sequence to use for templating
      files. valid choices are "\n", "\r", "\r\n". Default value "\n".'
    - 'C(block_start_string) (str): The string marking the beginning of a block. Default
      value "{%".'
    - 'C(block_end_string) (str): The string marking the end of a block. Default value
      "%}".'
    - 'C(variable_start_string) (str): The string marking the beginning of a print
      statement. Default value "{{".'
    - 'C(variable_end_string) (str): The string marking the end of a print statement.
      Default value "}}".'
    - 'C(trim_blocks) (bool): Determine when newlines should be removed from blocks.
      When set to C(yes) the first newline after a block is removed (block, not variable
      tag!). Default value is true.'
    - 'C(lstrip_blocks) (bool): Determine when leading spaces and tabs should be stripped.
      When set to C(yes) leading spaces and tabs are stripped from the start of a
      line to a block. This functionality requires Jinja 2.7 or newer. Default value
      is false.'
    type: raw
    version_added: 2.0.0
    version_added_collection: redhat.openshift
  username:
    description:
    - Provide a username for authenticating with the API. Can also be specified via
      K8S_AUTH_USERNAME environment variable.
    - Please note that this only works with clusters configured to use HTTP Basic
      Auth. If your cluster has a different form of authentication (e.g. OAuth2 in
      OpenShift), this option will not work as expected and you should look into the
      M(community.okd.k8s_auth) module, as that might do what you need.
    type: str
  validate:
    description:
    - how (if at all) to validate the resource definition against the kubernetes schema.
      Requires the kubernetes-validate python module
    suboptions:
      fail_on_error:
        description: whether to fail on validation errors.
        type: bool
      strict:
        default: true
        description: whether to fail when passing unexpected properties
        type: bool
      version:
        description: version of Kubernetes to validate against. defaults to Kubernetes
          server version
        type: str
    type: dict
  validate_certs:
    aliases:
    - verify_ssl
    description:
    - Whether or not to verify the API server's SSL certificates. Can also be specified
      via K8S_AUTH_VERIFY_SSL environment variable.
    type: bool
  wait:
    default: false
    description:
    - Whether to wait for certain resource kinds to end up in the desired state.
    - By default the module exits once Kubernetes has received the request.
    - Implemented for C(state=present) for C(Deployment), C(DaemonSet) and C(Pod),
      and for C(state=absent) for all resource kinds.
    - For resource kinds without an implementation, C(wait) returns immediately unless
      C(wait_condition) is set.
    type: bool
  wait_condition:
    description:
    - Specifies a custom condition on the status to wait for.
    - Ignored if C(wait) is not set or is set to False.
    suboptions:
      reason:
        description:
        - The value of the reason field in your desired condition
        - For example, if a C(Deployment) is paused, The C(Progressing) C(type) will
          have the C(DeploymentPaused) reason.
        - The possible reasons in a condition are specific to each resource type in
          Kubernetes.
        - See the API documentation of the status field for a given resource to see
          possible choices.
        type: str
      status:
        choices:
        - 'True'
        - 'False'
        - Unknown
        default: 'True'
        description:
        - The value of the status field in your desired condition.
        - For example, if a C(Deployment) is paused, the C(Progressing) C(type) will
          have the C(Unknown) status.
        type: str
      type:
        description:
        - The type of condition to wait for.
        - For example, the C(Pod) resource will set the C(Ready) condition (among
          others).
        - Required if you are specifying a C(wait_condition).
        - If left empty, the C(wait_condition) field will be ignored.
        - The possible types for a condition are specific to each resource type in
          Kubernetes.
        - See the API documentation of the status field for a given resource to see
          possible choices.
        type: str
    type: dict
  wait_sleep:
    default: 5
    description:
    - Number of seconds to sleep between checks.
    type: int
  wait_timeout:
    default: 120
    description:
    - How long in seconds to wait for the resource to end up in the desired state.
    - Ignored if C(wait) is not set.
    type: int
requirements:
- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11
short_description: Manage OpenShift objects
'''

EXAMPLES = '''

- name: Create a k8s namespace
  redhat.openshift.k8s:
    name: testing
    api_version: v1
    kind: Namespace
    state: present

- name: Create a Service object from an inline definition
  redhat.openshift.k8s:
    state: present
    definition:
      apiVersion: v1
      kind: Service
      metadata:
        name: web
        namespace: testing
        labels:
          app: galaxy
          service: web
      spec:
        selector:
          app: galaxy
          service: web
        ports:
        - protocol: TCP
          targetPort: 8000
          name: port-8000-tcp
          port: 8000

- name: Remove an existing Service object
  redhat.openshift.k8s:
    state: absent
    api_version: v1
    kind: Service
    namespace: testing
    name: web

# Passing the object definition from a file

- name: Create a Deployment by reading the definition from a local file
  redhat.openshift.k8s:
    state: present
    src: /testing/deployment.yml

- name: >-
    Read definition file from the Ansible controller file system.
    If the definition file has been encrypted with Ansible Vault it will automatically be decrypted.
  redhat.openshift.k8s:
    state: present
    definition: "{{ lookup('file', '/testing/deployment.yml') | from_yaml }}"

- name: Read definition file from the Ansible controller file system after Jinja templating
  redhat.openshift.k8s:
    state: present
    definition: "{{ lookup('template', '/testing/deployment.yml') | from_yaml }}"

- name: fail on validation errors
  redhat.openshift.k8s:
    state: present
    definition: "{{ lookup('template', '/testing/deployment.yml') | from_yaml }}"
    validate:
      fail_on_error: yes

- name: warn on validation errors, check for unexpected properties
  redhat.openshift.k8s:
    state: present
    definition: "{{ lookup('template', '/testing/deployment.yml') | from_yaml }}"
    validate:
      fail_on_error: no
      strict: yes
'''

RETURN = '''
result:
  contains:
    api_version:
      description: The versioned schema of this representation of an object.
      returned: success
      type: str
    duration:
      description: elapsed time of task in seconds
      returned: when C(wait) is true
      sample: 48
      type: int
    error:
      description: error while trying to create/delete the object.
      returned: error
      type: complex
    items:
      description: Returned only when multiple yaml documents are passed to src or
        resource_definition
      returned: when resource_definition or src contains list of objects
      type: list
    kind:
      description: Represents the REST resource this object represents.
      returned: success
      type: str
    metadata:
      description: Standard object metadata. Includes name, namespace, annotations,
        labels, etc.
      returned: success
      type: complex
    spec:
      description: Specific attributes of the object. Will vary based on the I(api_version)
        and I(kind).
      returned: success
      type: complex
    status:
      description: Current status details for the object.
      returned: success
      type: complex
  description:
  - The created, patched, or otherwise present object. Will be empty in the case of
    a deletion.
  returned: success
  type: complex
'''


import copy
import re
import operator
import traceback
from functools import reduce

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native

try:
    from ansible_collections.kubernetes.core.plugins.module_utils.common import get_api_client, K8sAnsibleMixin
    from ansible_collections.kubernetes.core.plugins.module_utils.args_common import (
        NAME_ARG_SPEC, RESOURCE_ARG_SPEC, AUTH_ARG_SPEC, WAIT_ARG_SPEC, DELETE_OPTS_ARG_SPEC)
    HAS_KUBERNETES_COLLECTION = True
except ImportError as e:
    HAS_KUBERNETES_COLLECTION = False
    k8s_collection_import_exception = e
    K8S_COLLECTION_ERROR = traceback.format_exc()

try:
    import yaml
    from kubernetes.dynamic.exceptions import DynamicApiError, NotFoundError, ForbiddenError
except ImportError:
    # Exceptions handled in common
    pass

TRIGGER_ANNOTATION = 'image.openshift.io/triggers'
TRIGGER_CONTAINER = re.compile(r"(?P<path>.*)\[((?P<index>[0-9]+)|\?\(@\.name==[\"'\\]*(?P<name>[a-z0-9]([-a-z0-9]*[a-z0-9])?))")


class OKDRawModule(K8sAnsibleMixin):

    def __init__(self, k8s_kind=None, *args, **kwargs):
        mutually_exclusive = [
            ('resource_definition', 'src'),
            ('merge_type', 'apply'),
            ('template', 'resource_definition'),
            ('template', 'src'),
        ]

        module = AnsibleModule(
            argument_spec=self.argspec,
            mutually_exclusive=mutually_exclusive,
            supports_check_mode=True,
        )

        self.module = module
        self.check_mode = self.module.check_mode
        self.params = self.module.params
        self.fail_json = self.module.fail_json
        self.fail = self.module.fail_json
        self.exit_json = self.module.exit_json

        if not HAS_KUBERNETES_COLLECTION:
            self.fail_json(
                msg="The kubernetes.core collection must be installed",
                exception=K8S_COLLECTION_ERROR,
                error=to_native(k8s_collection_import_exception)
            )

        super(OKDRawModule, self).__init__(module, *args, **kwargs)

        self.client = get_api_client(module)
        self.warnings = []

        self.kind = k8s_kind or self.params.get('kind')
        self.api_version = self.params.get('api_version')
        self.name = self.params.get('name')
        self.namespace = self.params.get('namespace')

        self.check_library_version()
        self.set_resource_definitions(module)

    @property
    def validate_spec(self):
        return dict(
            fail_on_error=dict(type='bool'),
            version=dict(),
            strict=dict(type='bool', default=True)
        )

    @property
    def argspec(self):
        argument_spec = copy.deepcopy(NAME_ARG_SPEC)
        argument_spec.update(copy.deepcopy(RESOURCE_ARG_SPEC))
        argument_spec.update(copy.deepcopy(AUTH_ARG_SPEC))
        argument_spec.update(copy.deepcopy(WAIT_ARG_SPEC))
        argument_spec['merge_type'] = dict(type='list', elements='str', choices=['json', 'merge', 'strategic-merge'])
        argument_spec['validate'] = dict(type='dict', default=None, options=self.validate_spec)
        argument_spec['append_hash'] = dict(type='bool', default=False)
        argument_spec['apply'] = dict(type='bool', default=False)
        argument_spec['template'] = dict(type='raw', default=None)
        argument_spec['delete_options'] = dict(type='dict', default=None, options=copy.deepcopy(DELETE_OPTS_ARG_SPEC))
        argument_spec['continue_on_error'] = dict(type='bool', default=False)
        argument_spec['state'] = dict(default='present', choices=['present', 'absent', 'patched'])
        argument_spec['force'] = dict(type='bool', default=False)
        return argument_spec

    def perform_action(self, resource, definition):
        state = self.params.get('state', None)
        name = definition['metadata'].get('name')
        namespace = definition['metadata'].get('namespace')

        if state != 'absent':

            if resource.kind in ['Project', 'ProjectRequest']:
                try:
                    resource.get(name, namespace)
                except (NotFoundError, ForbiddenError):
                    return self.create_project_request(definition)
                except DynamicApiError as exc:
                    self.fail_json(msg='Failed to retrieve requested object: {0}'.format(exc.body),
                                   error=exc.status, status=exc.status, reason=exc.reason)

            try:
                existing = resource.get(name=name, namespace=namespace).to_dict()
            except Exception:
                existing = None

            if existing:
                if resource.kind == 'DeploymentConfig':
                    if definition.get('spec', {}).get('triggers'):
                        definition = self.resolve_imagestream_triggers(existing, definition)
                elif existing['metadata'].get('annotations', {}).get(TRIGGER_ANNOTATION):
                    definition = self.resolve_imagestream_trigger_annotation(existing, definition)

        return super(OKDRawModule, self).perform_action(resource, definition)

    @staticmethod
    def get_index(desired, objects, keys):
        """ Iterates over keys, returns the first object from objects where the value of the key
            matches the value in desired
        """
        for i, item in enumerate(objects):
            if item and all([desired.get(key, True) == item.get(key, False) for key in keys]):
                return i

    def resolve_imagestream_trigger_annotation(self, existing, definition):

        def get_from_fields(d, fields):
            try:
                return reduce(operator.getitem, fields, d)
            except Exception:
                return None

        def set_from_fields(d, fields, value):
            get_from_fields(d, fields[:-1])[fields[-1]] = value

        if TRIGGER_ANNOTATION in definition['metadata'].get('annotations', {}).keys():
            triggers = yaml.safe_load(definition['metadata']['annotations'][TRIGGER_ANNOTATION] or '[]')
        else:
            triggers = yaml.safe_load(existing['metadata'].get('annotations', '{}').get(TRIGGER_ANNOTATION, '[]'))

        if not isinstance(triggers, list):
            return definition

        for trigger in triggers:
            if trigger.get('fieldPath'):
                parsed = self.parse_trigger_fieldpath(trigger['fieldPath'])
                path = parsed.get('path', '').split('.')
                if path:
                    existing_containers = get_from_fields(existing, path)
                    new_containers = get_from_fields(definition, path)
                    if parsed.get('name'):
                        existing_index = self.get_index({'name': parsed['name']}, existing_containers, ['name'])
                        new_index = self.get_index({'name': parsed['name']}, new_containers, ['name'])
                    elif parsed.get('index') is not None:
                        existing_index = new_index = int(parsed['index'])
                    else:
                        existing_index = new_index = None
                    if existing_index is not None and new_index is not None:
                        if existing_index < len(existing_containers) and new_index < len(new_containers):
                            set_from_fields(definition, path + [new_index, 'image'], get_from_fields(existing, path + [existing_index, 'image']))
        return definition

    def resolve_imagestream_triggers(self, existing, definition):

        existing_triggers = existing.get('spec', {}).get('triggers')
        new_triggers = definition['spec']['triggers']
        existing_containers = existing.get('spec', {}).get('template', {}).get('spec', {}).get('containers', [])
        new_containers = definition.get('spec', {}).get('template', {}).get('spec', {}).get('containers', [])
        for i, trigger in enumerate(new_triggers):
            if trigger.get('type') == 'ImageChange' and trigger.get('imageChangeParams'):
                names = trigger['imageChangeParams'].get('containerNames', [])
                for name in names:
                    old_container_index = self.get_index({'name': name}, existing_containers, ['name'])
                    new_container_index = self.get_index({'name': name}, new_containers, ['name'])
                    if old_container_index is not None and new_container_index is not None:
                        image = existing['spec']['template']['spec']['containers'][old_container_index]['image']
                        definition['spec']['template']['spec']['containers'][new_container_index]['image'] = image

                    existing_index = self.get_index(trigger['imageChangeParams'],
                                                    [x.get('imageChangeParams') for x in existing_triggers],
                                                    ['containerNames'])
                    if existing_index is not None:
                        existing_image = existing_triggers[existing_index].get('imageChangeParams', {}).get('lastTriggeredImage')
                        if existing_image:
                            definition['spec']['triggers'][i]['imageChangeParams']['lastTriggeredImage'] = existing_image
                        existing_from = existing_triggers[existing_index].get('imageChangeParams', {}).get('from', {})
                        new_from = trigger['imageChangeParams'].get('from', {})
                        existing_namespace = existing_from.get('namespace')
                        existing_name = existing_from.get('name', False)
                        new_name = new_from.get('name', True)
                        add_namespace = existing_namespace and 'namespace' not in new_from.keys() and existing_name == new_name
                        if add_namespace:
                            definition['spec']['triggers'][i]['imageChangeParams']['from']['namespace'] = existing_from['namespace']

        return definition

    def parse_trigger_fieldpath(self, expression):
        parsed = TRIGGER_CONTAINER.search(expression).groupdict()
        if parsed.get('index'):
            parsed['index'] = int(parsed['index'])
        return parsed

    def create_project_request(self, definition):
        definition['kind'] = 'ProjectRequest'
        result = {'changed': False, 'result': {}}
        resource = self.find_resource('ProjectRequest', definition['apiVersion'], fail=True)
        if not self.check_mode:
            try:
                k8s_obj = resource.create(definition)
                result['result'] = k8s_obj.to_dict()
            except DynamicApiError as exc:
                self.fail_json(msg="Failed to create object: {0}".format(exc.body),
                               error=exc.status, status=exc.status, reason=exc.reason)
        result['changed'] = True
        result['method'] = 'create'
        return result


def main():
    OKDRawModule().execute_module()


if __name__ == '__main__':
    main()
