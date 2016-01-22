#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keystoneclient.v2_0.client as ksclient
from novaclient import client as noclient
import ConfigParser, time 


config = ConfigParser.ConfigParser()
config.read('config.ini')
print(config.sections())

os_username = config.get('OPENSTACK_CREDENTIALS', 'os.username')
os_password = config.get('OPENSTACK_CREDENTIALS', 'os.password')
os_tenant = config.get('OPENSTACK_CREDENTIALS', 'os.tenant')
os_auth_url = config.get('OPENSTACK_CREDENTIALS', 'os.auth_url')

KEYSTONE_CONN = ksclient.Client(
                    auth_url=os_auth_url,
                    username=os_username,
                    password=os_password,
                    tenant=os_tenant)

print(KEYSTONE_CONN.authenticate())

OS_TOKEN = KEYSTONE_CONN.get_token(KEYSTONE_CONN.session)
RAW_TOKEN = KEYSTONE_CONN.get_raw_token_from_identity_service(
            auth_url=os_auth_url,
            username=os_username,
            password=os_password,
            tenant_name=os_tenant)

os_tenant_id = RAW_TOKEN['token']['tenant']['id']

NOVA_CONN = noclient.Client('1.1',
                            auth_url=os_auth_url,
                            username=os_username,
                            auth_token=OS_TOKEN,
                            tenant_id=os_tenant_id)

print(NOVA_CONN.servers.list())

KP_MANAGER = NOVA_CONN.keypairs
SG_MANAGER = NOVA_CONN.security_groups
RULE_MANAGER = NOVA_CONN.security_group_rules

#vm_credentials = dict(config['SSH_CREDENTIALS'])
ssh_username = config.get('SSH_CREDENTIALS', 'ssh.username')
ssh_password = config.get('SSH_CREDENTIALS', 'ssh.password')
ssh_public_key_filename = config.get('SSH_CREDENTIALS', 'ssh.public_key_filename')

public_key = [line for line in
                    open(ssh_public_key_filename)][0]

if not(KP_MANAGER.findall(name='test_key')):
    pk = KP_MANAGER.create('test_key', public_key=public_key)
else:
    pk = KP_MANAGER.findall(name='test_key')[0]

sg_new = False
if not(SG_MANAGER.findall(name='webserver')):
    sec_group = SG_MANAGER.create('webserver',
                'Allows SSH and web server access.')
    sg_new = True
else:
    sec_group = SG_MANAGER.findall(name='webserver')[0]

if (sg_new):
    RULE_MANAGER.create(sec_group.id,
                        ip_protocol='tcp',
                        from_port=22,
                        to_port=22)
    RULE_MANAGER.create(sec_group.id,
                        ip_protocol='tcp',
                        from_port=80,
                        to_port=80)
    RULE_MANAGER.create(sec_group.id,
                        ip_protocol='icmp',
                        from_port=-1,
                        to_port=-1)

VM_MANAGER = NOVA_CONN.servers
IMAGE_MANAGER = NOVA_CONN.images
FLAVOR_MANAGER = NOVA_CONN.flavors
NETWORK_MANAGER = NOVA_CONN.networks

image = IMAGE_MANAGER.findall(name='cirros-0.3.3-x86_64')[0]
flavor = FLAVOR_MANAGER.findall(name='m1.tiny')[0]
network = NETWORK_MANAGER.findall(
                label='net1')[0]
nics = [{'net-id': network.id}]

if not (VM_MANAGER.findall(name='TestVM123')):
    vm = VM_MANAGER.create(name='TestVM123',
                        image=image.id,
                        flavor=flavor.id,
                        security_groups=[sec_group.human_id],
                        key_name=pk.name,
                        nics=nics,
                        availability_zone='nova')
else:
    vm = VM_MANAGER.findall(name='TestVM123')[0]

while (vm.status != 'ACTIVE'):
    vm = VM_MANAGER.findall(name='TestVM123')[0]
    if (vm.status == 'ERROR'):
        print("VM ID: %s name: %s CREATION FAILED!!" % (vm.id, vm.name))
        break
    print("VM ID: %s name: %s in status: %s" %
            (vm.id, vm.name, vm.status))
    time.sleep(1)

print("VM ID: %s name: %s CREATION SUCCESSFUL." % 
        (vm.id, vm.name))
