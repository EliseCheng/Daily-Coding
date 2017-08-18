#!/bin/bash
#提供网卡设置信息
#interfaces文件中添加eth0，eth1 …
sed –i '$a auto eth0' /etc/network/interfaces
sed –i '$a iface eth0 inet dhcp' /etc/network/interfaces
sed –i '$a auto eth1' /etc/network/interfaces
sed –i '$a iface eth1 inet dhcp' /etc/network/interfaces

#启动ovs
sudo ovsdb-server --remote=punix:/usr/local/var/run/openvswitch/db.sock \
	              --remote=db:Open_vSwitch,manager_options \
                 	  --private-key=db:SSL,private_key \
	              --certificate=db:SSL,certificate \
	              --bootstrap-ca-cert=db:SSL,ca_cert \
	              --pidfile --detach
	            
#网卡加到ovs网桥中
ovs-vsctl add-port br1 eth0
ovs-vsctl add-port br1 eth1
