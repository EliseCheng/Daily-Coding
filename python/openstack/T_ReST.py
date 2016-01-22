#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib
import json

ip_set = '192.168.5.203'


def get_identity():
    action = 'GET'
    url = "/v2.0"
    conn = httplib.HTTPConnection('192.168.5.203:5000')
    conn.request(action, url)
    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    print ret

def create_user():
    #do not have tenantID but could get token
    user_info = {
        "user": {
            "tenantId": "a54df5c205ae438f91779857d3ed0540",
            "username": "jqsmith",
            "email": "john.smith@example.org",
            "enabled": True,
            "OS-KSADM:password": "secrete"
        }
    }
    
    #do not have password and can't get token
    user_with_tenant = {
        "user": {
            "tenantId": "a54df5c205ae438f91779857d3ed0540",
            "name": "chengwen",
            "email": "chengwen@example.org",
            "enabled": True
        }
    }
    body = json.dumps(user_info)
    headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json',
                'X-Auth-Token': 2012
             }
    conn = httplib.HTTPConnection('192.168.5.203:35357')
    conn.request('POST', '/v2.0/users', body, headers)

    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    print ret

def send_request(ip, port, action, url, info):
    body = json.dumps(info)
    headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json',
                'X-Auth-Token': 2012
             }
    conn = httplib.HTTPConnection(ip, port)
    conn.request(action, url, body, headers)

    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    print ret

def get_token():
    auth_info = {
        "auth": {
            "passwordCredentials": {
                "username": "jqsmith",
                "password": "secrete"
         }
        }
    }
    
    send_request('192.168.5.203', 5000, 'POST', '/v2.0/tokens', auth_info)

def send_info(ip, port, action, url):
    conn = httplib.HTTPConnection(ip, port)
    conn.request(action, url, '', {'X-Auth-Token': '5affb249b6054c358bc71e7e20731331'})

    response = conn.getresponse()
    ret = (response.status, response.reason, response.read())
    print ret

def list_users():
    send_info(ip_set, 35357, 'GET', '/v2.0/users')

def list_tenants(): 
    send_info(ip_set, 35357, 'GET', '/v2.0/tenants')
    

def create_tenant():
    tenant = {
        "tenant": {
            "name": "mygroup1",
            "description": "test tenant1",
            "enabled": True
        }
    }
    send_request('192.168.5.203', 5000, 'POST', '/v2.0/tenants', tenant)

def delete_user():
    send_info('192.168.5.203', 35357, 'DELETE', '/v2.0/users/e52e76cdebfa417aaafd88d38dd3c72e') 


def list_compute_api():
    send_info(ip_set, 8774, 'GET', '/v2/a54df5c205ae438f91779857d3ed0540/servers') 

if __name__ == '__main__':
    #step 1:
    #list_tenants()

    #step2:
    #create_user()
    #get conflict

    #step3:
    #list_users() 
    #get user list, it contains the user we added

    #step4:
    #get_token()

    #delete_user()

    list_compute_api()
    

    
