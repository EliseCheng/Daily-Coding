#! /usr/bin/python
import imaplib  
import email  

'''
Get Email
'''
def extract_body(payload):  
    if isinstance(payload,str):  
        return payload  
    else:  
        return '\n'.join([extract_body(part.get_payload()) for part in payload])  
  
conn = imaplib.IMAP4_SSL("pop.gmail.com", 993)  
conn.login("chengwen.hs@gmail.com", "******")  
conn.select()  
#typ, data = conn.search(None, 'UNSEEN')  
typ, data = conn.search(None, 'UNSEEN', 'FROM', '"alice.cheng"', 'SUBJECT', '"again"')
try:  
    for num in data[0].split():  
        typ, msg_data = conn.fetch(num, '(RFC822)')  
        for response_part in msg_data:  
            if isinstance(response_part, tuple):  
                msg = email.message_from_string(response_part[1])  
                subject = msg['subject']                     
                print "Subject is " + subject  
                #payload = msg.get_payload()  
                #body = extract_body(payload)  
                #print(body + "\n")  
		#print payload
        typ, response = conn.store(num, '+FLAGS', r'(\Seen)') 
	#typ, response = conn.store(num, '+FLAGS', '\\SEEN')  
finally:  
    try:  
        conn.close()  
    except:  
        pass  
    conn.logout()
