'''
SMTP(simple mail transfer protocol)
----------------------------------
----------->> This is used to send emails from server to another.

note:
-----
1.smtp ssl port
--------
465

2.smtp tls port
--------
587

import smtplib(library)


emailmessage class
------------------
msg['subject']="SMTP ON MAIL"
msg['from']='sender@mail.com'
msg['to']='receiver@mail.com'

import smtplib
from email.message import EmailMessage
sender='karthikyedagiri@gmail.com'
password='ymhhuiemvtqpqnum'
msg=EmailMessage()
msg['Subject']='Welcome Mail'
msg['from']=sender
msg['To']='rohansai4645@gmail.com'
msg.set_content('frooti')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
'''
import smtplib
from email.message import EmailMessage
sender='karthikyedagiri@gmail.com'
password='uivixhhzmdlkiwlh'
receiver=['rohansai4645@gmail.com','nandigambadrinadh4@gmail.com']
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)

for email in receiver:
    msg=EmailMessage()
    msg['Subject']='Welcome Mail'
    msg['from']=sender
    msg['To']=email
    msg.set_content('morris garages')
    server.send_message(msg)
server.quit()    
