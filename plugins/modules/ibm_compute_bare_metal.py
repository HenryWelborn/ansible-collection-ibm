#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_bare_metal
short_description: Configure IBM Cloud 'ibm_compute_bare_metal' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_bare_metal' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.9.0
    - Terraform v0.12.20

options:
    domain:
        description:
            - (Required for new resource) Domain name
        required: True
        type: str
    package_key_name:
        description:
            - None
        required: False
        type: str
    os_key_name:
        description:
            - None
        required: False
        type: str
    notes:
        description:
            - Optional notes info
        required: False
        type: str
    fixed_config_preset:
        description:
            - Fixed config preset value
        required: False
        type: str
    extended_hardware_testing:
        description:
            - None
        required: False
        type: bool
        default: False
    hostname:
        description:
            - Host name
        required: False
        type: str
    ssh_key_ids:
        description:
            - SSH KEY IDS list
        required: False
        type: list
        elements: int
    user_metadata:
        description:
            - User metadata info
        required: False
        type: str
    image_template_id:
        description:
            - OS image template ID
        required: False
        type: int
    private_network_only:
        description:
            - only private network configured if is true
        required: False
        type: bool
        default: False
    ipv6_static_enabled:
        description:
            - boolean value true if ipv6 static is enabled else false
        required: False
        type: bool
        default: False
    software_guard_extensions:
        description:
            - None
        required: False
        type: bool
        default: False
    disk_key_names:
        description:
            - None
        required: False
        type: list
        elements: str
    storage_groups:
        description:
            - None
        required: False
        type: list
        elements: dict
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    network_speed:
        description:
            - Network speed in MBPS
        required: False
        type: int
        default: 100
    hourly_billing:
        description:
            - Enables hourly billing
        required: False
        type: bool
        default: True
    tcp_monitoring:
        description:
            - TCP monitoring enabled if set as true
        required: False
        type: bool
        default: False
    process_key_name:
        description:
            - None
        required: False
        type: str
    restricted_network:
        description:
            - None
        required: False
        type: bool
        default: False
    secondary_ip_count:
        description:
            - Secondary IP addresses count
        required: False
        type: int
    ipv6_enabled:
        description:
            - Boolean value true if IPV6 ia enabled or false
        required: False
        type: bool
        default: False
    redundant_network:
        description:
            - None
        required: False
        type: bool
        default: False
    gpu_key_name:
        description:
            - None
        required: False
        type: str
    gpu_secondary_key_name:
        description:
            - None
        required: False
        type: str
    unbonded_network:
        description:
            - None
        required: False
        type: bool
        default: False
    quote_id:
        description:
            - Quote ID for Quote based provisioning
        required: False
        type: int
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('domain', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'domain',
    'package_key_name',
    'os_key_name',
    'notes',
    'fixed_config_preset',
    'extended_hardware_testing',
    'hostname',
    'ssh_key_ids',
    'user_metadata',
    'image_template_id',
    'private_network_only',
    'ipv6_static_enabled',
    'software_guard_extensions',
    'disk_key_names',
    'storage_groups',
    'post_install_script_uri',
    'tags',
    'network_speed',
    'hourly_billing',
    'tcp_monitoring',
    'process_key_name',
    'restricted_network',
    'secondary_ip_count',
    'ipv6_enabled',
    'redundant_network',
    'gpu_key_name',
    'gpu_secondary_key_name',
    'unbonded_network',
    'quote_id',
]

# Params for Data source 
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
    'image_template_id':  ['os_reference_code'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    domain=dict(
        required= False,
        type='str'),
    package_key_name=dict(
        required= False,
        type='str'),
    os_key_name=dict(
        required= False,
        type='str'),
    notes=dict(
        required= False,
        type='str'),
    fixed_config_preset=dict(
        required= False,
        type='str'),
    extended_hardware_testing=dict(
        required= False,
        type='bool'),
    hostname=dict(
        required= False,
        type='str'),
    ssh_key_ids=dict(
        required= False,
        elements='',
        type='list'),
    user_metadata=dict(
        required= False,
        type='str'),
    image_template_id=dict(
        required= False,
        type='int'),
    private_network_only=dict(
        required= False,
        type='bool'),
    ipv6_static_enabled=dict(
        required= False,
        type='bool'),
    software_guard_extensions=dict(
        required= False,
        type='bool'),
    disk_key_names=dict(
        required= False,
        elements='',
        type='list'),
    storage_groups=dict(
        required= False,
        elements='',
        type='list'),
    post_install_script_uri=dict(
        required= False,
        type='str'),
    tags=dict(
        required= False,
        elements='',
        type='list'),
    network_speed=dict(
        required= False,
        type='int'),
    hourly_billing=dict(
        required= False,
        type='bool'),
    tcp_monitoring=dict(
        required= False,
        type='bool'),
    process_key_name=dict(
        required= False,
        type='str'),
    restricted_network=dict(
        required= False,
        type='bool'),
    secondary_ip_count=dict(
        required= False,
        type='int'),
    ipv6_enabled=dict(
        required= False,
        type='bool'),
    redundant_network=dict(
        required= False,
        type='bool'),
    gpu_key_name=dict(
        required= False,
        type='str'),
    gpu_secondary_key_name=dict(
        required= False,
        type='str'),
    unbonded_network=dict(
        required= False,
        type='bool'),
    quote_id=dict(
        required= False,
        type='int'),
    id=dict(
        required= False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))


    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
         module.fail_json(msg=("conflicts exists: {}".format(conflicts)))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_compute_bare_metal',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.9.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] != None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_compute_bare_metal',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.9.0',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)

def main():
    run_module()


if __name__ == '__main__':
    main()
