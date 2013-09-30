#!/usr/bin/env python
import urllib

google = urllib.urlopen('http://www.baidu.com')
print 'http header:/n', google.info()
print 'http status:', google.getcode()
print 'url:', google.geturl()
#for line in google:
    #print line,
google.close()
