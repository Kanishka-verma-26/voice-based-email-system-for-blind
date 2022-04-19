from bs4 import BeautifulSoup
import email
import base64

import imaplib
from gtts import gTTS
import pyglet
import os, time




email_user = "khashstudioz@gmail.com"
email_pass = "Kanimilky@21697"
mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(email_user, email_pass)
mail.select()
type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()
for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet...
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('/Users/sanketdoshi/python/', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))





#
# def readmails():
#     mail = imaplib.IMAP4_SSL('imap.gmail.com',993)                                                    #this is host and port area.... ssl security
#     unm = ('khashstudioz@gmail.com')                                                                 #username
#     psw = ('Kanimilky@21697')                                                                        #password
#     mail.login(unm,psw)                                                                                     #login
#     print("logged in")
#     stat, total = mail.select('Inbox')                                                              #total number of mails in inbox
#     print ("Number of mails in your inbox :"+str(total))
#
#     #unseen mails
#     unseen = mail.search(None, '(UNSEEN)')
#     print(unseen)
#     # typ, data = mail.uid('fetch', b'3', '(RFC822)')
#     # print(typ, data)
#
#     # print(unseen[1])                                     # unseen count
#   #  print ("Number of UnSeen mails :"+str(unseen))
#
#     print()
#
#
#
#     #search mails
#     result, data = mail.uid('search',None, "ALL")
#     inbox_item_list = data[0].split()
#     print(inbox_item_list)
#     new = inbox_item_list[0]
#     old = inbox_item_list[0]
#     result2, email_data = mail.uid('fetch', new, '(RFC822)')                                                 #fetch
#     print("result :",result2)
#     print("data ",email_data)
#     print()
#     raw_email = email_data[0][1].decode("utf-8")                                                             #decode
#     email_message = email.message_from_string(raw_email)
#     print ("From: "+email_message['From'])
#     print ("Subject: "+str(email_message['Subject']))
#
#
#     #Body part of mails
#     stat, total1 = mail.select('Inbox')
#     stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
#     msg = data1[0][1]
#     soup = BeautifulSoup(msg, "html.parser")
#     txt = soup.get_text()
#     print ("Body :"+txt)
#     mail.close()
#     mail.logout()
#     print("prinnted")
#
# readmails()
