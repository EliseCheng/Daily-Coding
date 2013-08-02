#!/bin/bash
#192.168.5.107
#关闭nignx
ps -ef| grep nginx | awk '$3==1 {print $2}' | xargs kill -QUIT
#重启nginx（不加速）
/usr/local/nginx/nginx

#关闭nignx
ps -ef| grep nginx | awk '$3==1 {print $2}' | xargs kill -QUIT
#重启nginx（加速）
/usr/local/nginx/nginx -c nginx_cache.conf







