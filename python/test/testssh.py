import base64
import struct
openssh_pubkey = open('keyfile').read()

type, key_string, comment = openssh_pubkey.split()
data = base64.decodestring(key_string)
int_len = 4
str_len = struct.unpack('>I', data[:int_len])[0] # this should return 7
print data[int_len:int_len+str_len] == type
