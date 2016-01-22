#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser, time
from novaclient import client as noclient

config = ConfigParser.ConfigParser()
config.read('config.ini')

#import pdb; pdb.set_trace()
NOVA_CONN  = noclient.Client('1.1', auth_url='http://172.72.72.22:8774/v1.1')
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

image = IMAGE_MANAGER.findall(name='Zmxvb2RsaWdodA==')[0]
flavor = FLAVOR_MANAGER.findall(name='m1.medium')[0]
#network = NETWORK_MANAGER.findall(
                #label='net1')[0]
#nics = [{'net-id': network.id}]

if not (VM_MANAGER.findall(name='myvm5')):
    vm = VM_MANAGER.create(name='myvm5',
                        image=image.id,
                        flavor=flavor.id,
                        security_groups=[sec_group.human_id],
                        #key_name=pk.name,
                        #nics=nics,
                        #availability_zone='nova'
                        )
else:
    vm = VM_MANAGER.findall(name='myvm5')[0]

while (vm.status != 'ACTIVE'):
    vm = VM_MANAGER.findall(name='myvm5')[0]
    if (vm.status == 'ERROR'):
        print("VM ID: %s name: %s CREATION FAILED!!" % (vm.id, vm.name))
        break
    print("VM ID: %s name: %s in status: %s" %
            (vm.id, vm.name, vm.status))
    print '-----------------------------'
    print VM_MANAGER.list()
    time.sleep(1)

