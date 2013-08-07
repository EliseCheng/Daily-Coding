#!/bin/bash

if [ `whoami` != "root" ]; then
	echo "需要root权限！"
	echo "退出..."
	exit
fi

if [ ! -f libvirt-1.0.1.tar.gz ]  || [ ! -f qemu.conf ] || [ ! -f libvirtd.conf ] || [ ! -f libvirt-bin ];then
	echo "请检查文件： libvirt-1.0.1.tar.gz是libvirt安装包，qemu.conf, libvirtd.conf, libvirt-bin是修改好的配置文件，用来直接替换原有文件，请检查它们是否在当前目录下。"
	exit
fi 

apt-get update

apt-get install -y libvirt-bin

apt-get install gcc make pip pkg-config libxml2-dev libgnutls-dev virtinst libdevmapper-dev gnutls-bin libgnutls-dev pm-utils libyajl-dev libnl-dev python-lxmllibxslt1-dev

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

cd ../
service libvirt-bin restart

LIBVIRT_PRO=`netstat -anput | grep libvirtd`
if [ ! -n "$LIBVIRT_PRO" ];then
	echo "libvirt进程没有成功启动。"
else 
	echo $LIBVIRT_PRO
	echo "libvirt进程成功启动。"	
fi
echo "Waiting..." 
sleep 3
echo "=================设置远程访问libvirt=============="
apt-get install sasl2-bin
echo "设置访问libvirt的密码，用户名是root："
saslpasswd2 -a libvirt root

echo "验证用户名密码设置是否成功："
sasldblistusers2 -f /etc/libvirt/passwd.db

echo "验证连接libvirt命令"
virsh -c qemu+tcp://127.0.0.1/system
echo "看到virsh的欢迎提示了吗？有的话就成功了哦！:)"

echo "===========开始安装glance=========="
sleep 2
wget https://github.com/openstack/glance/archive/2012.2.4.zip
unzip 2012.2.4.zip
cd glance-2012.2.4 
python setup.py build
sudo python setup.py install








