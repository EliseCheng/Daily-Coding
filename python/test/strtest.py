#!/usr/bin/python
import os
print os.path.dirname(os.path.abspath(__file__))
'''select number from string'''
str_test = "A1B2C3"
str_list = list(str_test)
for i in range(len(str_list)):
    if ord(str_list[i]) in range(48, 58): #compare with ascii code
        print str_list[i]
