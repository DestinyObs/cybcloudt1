# Copyright © 2018 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause OR GPL-3.0-only

# !/usr/bin/python

from pyvcloud.vcd.org import Org
from pyvcloud.vcd.client import NSMAP
from ansible.module_utils.vcd import VcdAnsibleModule
from pyvcloud.vcd.exceptions import EntityNotFoundException


VCD_CATALOG_STATES = ['present', 'absent', 'update']
VCD_CATALOG_OPERATIONS = ['read', 'shared', 'list_items']


def vcd_catalog_argument_spec():
    return dict(
        catalog_name=dict(type='str', required=True),
        new_catalog_name=dict(type='str', required=False),
        description=dict(type='str', required=False),
        shared=dict(type='bool', required=False, default=True),
        org_name=dict(type='str', required=False, default=None),
        state=dict(choices=VCD_CATALOG_STATES, required=False),
        operation=dict(choices=VCD_CATALOG_OPERATIONS, required=False)
    )


class Catalog(VcdAnsibleModule):
    def __init__(self, **kwargs):
        super(Catalog, self).__init__(**kwargs)
        self.org = self.get_org()

    def manage_states(self):
        state = self.params.get('state')
        if state == "present":
            return self.create()

        if state == "absent":
            return self.delete()

        if state == "update":
            return self.update()

    def manage_operations(self):
        operation = self.params.get('operation')
        if operation == "shared":
            return self.shared()

        if operation == "read":
            return self.read()

        if operation == "list_items":
            return self.list_items()

    def get_org(self):
        org_name = self.params.get('org_name')
        org_resource = self.client.get_org()
        if org_name:
            org_resource = self.client.get_org_by_name(org_name)

        return Org(self.client, resource=org_resource)

    def create(self):
        catalog_name = self.params.get('catalog_name')
        description = self.params.get('description')
        response = dict()
        response['changed'] = False

        try:
            self.org.get_catalog(name=catalog_name)
        except EntityNotFoundException:
            self.org.create_catalog(name=catalog_name, description=description)
            msg = 'Catalog {} has been created.'
            response['msg'] = msg.format(catalog_name)
            response['changed'] = True
        else:
            msg = 'Catalog {} is already present.'
            response['warnings'] = msg.format(catalog_name)

        return response

    def delete(self):
        catalog_name = self.params.get('catalog_name')
        response = dict()
        response['changed'] = False

        try:
            self.org.get_catalog(name=catalog_name)
        except EntityNotFoundException:
            msg = 'Catalog {} is not present.'
            response['warnings'] = msg.format(catalog_name)
        else:
            self.org.delete_catalog(catalog_name)
            msg = 'Catalog {} has been deleted.'
            response['msg'] = msg.format(catalog_name)
            response['changed'] = True

        return response

    def update(self):
        catalog_name = self.params.get('catalog_name')
        new_catalog_name = self.params.get('new_catalog_name')
        description = self.params.get('description')
        response = dict()
        response['changed'] = False

        if not new_catalog_name:
            new_catalog_name = catalog_name

        self.org.update_catalog(old_catalog_name=catalog_name,
                                new_catalog_name=new_catalog_name,
                                description=description)
        response['msg'] = 'Catalog {} has been updated.'.format(catalog_name)
        response['changed'] = True

        return response

    def shared(self):
        catalog_name = self.params.get('catalog_name')
        shared = self.params.get('shared')
        response = dict()
        response['changed'] = False

        self.org.share_catalog(name=catalog_name, share=shared)
        msg = 'Catalog {} shared state has been updated to [shared={}].'
        response['msg'] = msg.format(catalog_name, shared)
        response['changed'] = True

        return response

    def read(self):
        catalog_name = self.params.get('catalog_name')
        response = dict()
        result = dict()
        response['changed'] = False

        catalog = self.org.get_catalog(catalog_name)
        result['name'] = str(catalog.get("name"))
        result['description'] = str(catalog.Description)
        result['shared'] = str(catalog.IsPublished)
        response['msg'] = result

        return response

    def list_items(self):
        catalog_name = self.params.get('catalog_name')
        response = dict()
        response['changed'] = False

        catalog_items = self.org.list_catalog_items(catalog_name)
        response['msg'] = [catalog_item['name']
                           for catalog_item in catalog_items]

        return response


def main():
    argument_spec = vcd_catalog_argument_spec()
    response = dict(msg=dict(type='str'))
    module = Catalog(argument_spec=argument_spec, supports_check_mode=True)

    try:
        if module.check_mode:
            response = dict()
            response['changed'] = False
            response['msg'] = "skipped, running in check mode"
            response['skipped'] = True
        elif module.params.get('state'):
            response = module.manage_states()
        elif module.params.get('operation'):
            response = module.manage_operations()
        else:
            raise Exception('Please provide state/operation for resource')
    except Exception as error:
        response['msg'] = error.__str__()
        module.fail_json(**response)
    else:
        module.exit_json(**response)


if __name__ == '__main__':
    main()
