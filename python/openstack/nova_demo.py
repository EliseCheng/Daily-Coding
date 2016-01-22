#!/usr/bin/env python
# -*- coding: utf-8 -*-

from novaclient import client as nova_client
from neutronclient.neutron import client as neutron_client

nova = nova_client.Client('1.1', auth_url='http://172.171.4.22:8774/v1.1')
neutron = neutron_client.Client('2.0', endpoint_url='http://172.171.4.22:9696', auth_strategy='noauth')

class VM(object):
    servers = nova.servers

    def create(self, name, image, flavor, nics):
        """ Create vm instance
        
        :param name: name of vm instance.
        :param image: image to boot with.
        :param flavor: flavor to boot onto.
        :nics: a network id list of vm instance for creating interfaces 
            
        """
        servers.create(name, image, flavor, nics=nics)


        

flat_network = {'network': {'name':'flat_network', 'admin_state_up': True, 'tenant_id': 'admin', 'provider:network_type':'flat', 'provider:physical_network': 'physnet1' }}

gre_network = {'network': {'name':'gre_network', 'tenant_id': 'admin'}}
vxlan_network = {'network': {'name':'vxlan_network', 'tenant_id': 'admin'}}

ext_network = {'network': {'name':'ext_network',   'tenant_id': 'admin', 'router:external': True,
                           'provider:network_type':'flat', 'provider:physical_network': 'external' }}

tun_network = {'network': {'name':'tun_network', 'admin_state_up': True,  'tenant_id': 'admin'}

test_network = {'network': {'name':'test_network', 'admin_state_up': True,  'tenant_id': 'admin'}

neutron.create_network(flat_network)

subnet = {
    "subnet": {
        "network_id": "02bfc93c-79ab-481c-82f8-d57d1c2cd0fd",
        "ip_version": 4,
        "cidr": "172.171.0.1/20",
        'enable_dhcp': False,
        'gateway_ip' : '172.171.0.1',
        'allocation_pools': [{'start':'172.171.4.150','end':'172.171.4.160'}],
        'tenant_id': 'admin'
    }
}

subnet = {
    "subnet": {
        "network_id": "51430e2f-2064-400d-9b89-0af6e2e9fdab",
        "ip_version": 4,
        "cidr": "10.0.1.0/24",
        'tenant_id': 'admin',
        'enable_dhcp': True
    }
}


neutron.create_subnet(subnet)

neutron.list_security_groups()


my_secgroup = {'security_group': {"name": "new-webservers", "description": "security group for webservers", "tenant_id": "admin"}}
neutron.create_security_group(my_secgroup)

rule = {'security_group_rule': {'direction': 'ingress',
  'ethertype': 'IPv4',
  'port_range_max': 65535,
  'port_range_min': 1,
  'protocol': 'tcp',
  'remote_ip_prefix': '0.0.0.0/0',
  'remote_group_id': None,
  'security_group_id': '3777435e-556c-418b-ae17-273c75c18af1',
  'tenant_id': 'admin'}}

neutron.create_security_group_rule(rule)
neutron.list_networks()
#代码里面的过滤条件
#neutron.list_security_groups(**{"tenant_id": "admin"}) 



images = nova.images
flavors = nova.flavors

image = images.find(name='dWJ1bnR1')
flavor = flavors.find(name='m1.heat')


nics = [{'net-id': '51430e2f-2064-400d-9b89-0af6e2e9fdab'}]
nics=[{'net-id': 'ab0fed01-f9b8-460e-8a3b-38c7c5a61a41'}, {'net-id': 'd0856cc6-b201-433c-a8ae-9313a93590d7'}]


server.create(name='vm1', image=image.id, flavor=flavor.id, nics=nics)

servers.create(name='vm1', image=image.id, flavor=flavor.id, nics=nics)


router = {
    "router": {
        "name": "ext_router",
        "external_gateway_info": {
            "network_id": "02bfc93c-79ab-481c-82f8-d57d1c2cd0fd"
        },
        "tenant_id": "admin"
    }
}

router = {
    'router': {'name': 'router1', "tenant_id": "admin"}
}

neutron.add_gateway_router('f5d3da81-8842-49a3-9a4c-3096b33b9dc2', {'network_id': '02bfc93c-79ab-481c-82f8-d57d1c2cd0fd'})
neutron.remove_gateway_router('f5d3da81-8842-49a3-9a4c-3096b33b9dc2')
neutron.add_interface_router('f5d3da81-8842-49a3-9a4c-3096b33b9dc2', {"subnet_id": 'a897d034-c230-4e96-bdad-b645ad057103'})
neutron.update_port('745b6591-fd8b-4631-a0da-1107e891da7b',{'security_groups': ['3777435e-556c-418b-ae17-273c75c18af1']})

port = {
    'port': {
        'id': '66dd07fb-02a3-42fa-9aa3-a0f1fb68f4f1', 
        'security_groups': ['3777435e-556c-418b-ae17-273c75c18af1']    
    }
}

{
    "port": {
        "network_id": "f47eb8bd-074b-4364-b8e9-3c440ac466d1",
        "admin_state_up": True,
        "tenant_id" : "admin"
    }
}
