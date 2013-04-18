#! /usr/bin/python
# example of python docs
import imaplib

M = imaplib.IMAP4()
M.login("alice.cheng@neudigit.com", "*****")
M.select()
typ, date = M.search(None, "ALL")
for num in data[0].split():
	typ, data = M.fetch(num, '(RFC822)')
	print 'Message %s\n%s\n' % (num, data[0][1])
M.close()
M.logout()
