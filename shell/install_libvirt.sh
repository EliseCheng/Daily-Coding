#!/bin/bash

if [ `whoami` != "root" ]; then
	echo "需要root权限！"
	echo "退出..."
	exit
else [ ! -f libvirt-1.0.1.tar.gz ]  || [ ! -f qemu.conf ] || [ ! -f libvirtd.conf ] || [ ! -f libvirt-bin ]
	echo "请检查文件： libvirt-1.0.1.tar.gz, qemu.conf, libvirtd.conf, libvirt-bin 是否在当前目录下。"
	exit
fi 

apt-get update

apt-get install -y libvirt-bin

apt-get install gcc make pkg-config python-dev libxml2-dev libgnutls-dev libdevmapper-dev gnutls-bin libgnutls-dev virtinst pm-utils libyajl-dev libnl-dev

tar -zvxf libvirt-1.0.1.tar.gz
cd libvirt-1.0.1
./autogen.sh --system
make && make install

#用已经配置好的文件去替换原有的文件
echo "修改/etc/libvirt/libvirtd.conf 配置文件"
cp /etc/libvirt/libvirtd.conf /etc/libvirt/libvirtd.conf.bak
cp ../libvirtd.conf /etc/libvirt/libvirtd.conf

echo "修改/etc/libvirt/qemu.conf 配置文件"
cp /etc/libvirt/qemu.conf /etc/libvirt/qemu.conf.bak
cp ../qemu.conf /etc/libvirt/qemu.conf

echo 
cp /etc/default/libvirt-bin /etc/default/libvirt-bin.bak
cp ../libvirt-bin /etc/default/libvirt-bin

service libvirt-bin restart

LIBVIRT_PRO=`netstat -anput | grep libvirtd`
if [ ! -n $LIBVIRT_PRO ];then
	echo "libvirt进程没有成功启动。"
else 
	echo $LIBVIRT_PRO
	echo "libvirt进程成功启动。"	
fi 

echo "=================设置远程访问libvirt=============="
apt-get install sasl2-bin
echo "设置访问libvirt的用户名和密码："
saslpasswd2 -a libvirt root

echo "验证用户名密码设置是否成功："
sasldblistusers2 -f /etc/libvirt/passwd.db

echo "验证连接libvirt命令"
virsh -c qemu+tcp://127.0.0.1/system
echo "会看到virsh的欢迎提示，用quit命令退出。"








