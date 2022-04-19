# import imaplib, email
#
# user = 'khashstudioz@gmail.com'
# password = 'Kanimilky@21697'
# imap_url = 'imap.gmail.com'
#
#
# def get_body(msg):
#     if msg.is_multipart():
#         return get_body(msg.get_payload(0))
#     else:
#         return msg.get_payload(None, True)
#
# def search(key, value, con):
#     result, data = con.search(None, key, '"{}"'.format(value))
#     return data
#
# def get_emails(result_bytes):
#     msgs = []
#     for num in result_bytes[0].split():
#         typ, data = con.fetch(num, '(RFC822)')
#         msgs.append(data)
#     # print(msgs)
#     return msgs
#
# con = imaplib.IMAP4_SSL(imap_url)
# con.login(user, password)
# con.select('Inbox')
# msgs = get_emails(search('FROM', 'kanishka@hashstudioz.com', con))
# print(msgs)
#
# for msg in msgs[::-1]:
#     for sent in msg:
#         if type(sent) is tuple:
#
#             # encoding set as utf-8
#             content = str(sent[1], 'utf-8')
#             data = str(content)
#
#             try:
#                 indexstart = data.find("ltr")
#                 data2 = data[indexstart + 5: len(data)]
#                 indexend = data2.find("</div>")
#
#                 print(data2[0: indexend])
#
#             except UnicodeEncodeError as e:
#                 pass




import email
import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities) = mail.login('khashstudioz@gmail.com','Kanimilky@21697')
mail.list()
mail.select('inbox')

n=0
(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':

   for num in messages[0].split() :
      print ('Processing ')
      n=n+1
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_bytes(response_part[1])

            # print (original['From'])
            # print (original['Subject'])
             raw_email = data[0][1]
             raw_email_string = raw_email.decode('utf-8')
             email_message = email.message_from_string(raw_email_string)
             for part in email_message.walk():
                        if (part.get_content_type() == "text/plain"): # ignore attachments/html
                              body = part.get_payload(decode=True)
                              save_string = str(r"C:\Users\devda\Desktop\Internship\Dumpemail_" + str('richboy') + ".txt" )
                              myfile = open(save_string, 'a')
                              myfile.write(original['From']+'\n')
                              myfile.write(original['Subject']+'\n')
                              myfile.write(body.decode('utf-8'))
                              myfile.write('**********\n')
                              myfile.close()
                        else:
                            continue

             typ, data = mail.store(num, '+FLAGS', '\\Seen')

         print(n)