#!/bin/bash
 sed -i '$a auto eth1' /etc/network/interfaces
 sed -i '$a iface eth1 inet dhcp' /etc/network/interfaces
 ovs-vsctl add-br br0
 ovs-vsctl add-port br0 eth1
 ifconfig eth1 0 up
