from switftclient import client


"""
:preauthurl endpoint:publicURL
:preauthtoken keystone token
"""
conn = client.Connection(
    preauthurl='http://controller:8080/v1/AUTH_65f273a79a834498a87f3c51bd35bebf',              
    preauthtoken='2e1ab53724cc47c2bf100666e5d411d5'
)

