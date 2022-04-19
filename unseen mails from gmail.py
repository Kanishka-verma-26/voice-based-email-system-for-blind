# import required libraries
from bs4 import BeautifulSoup
import base64

import imaplib
import email
from email.header import decode_header
import webbrowser
import os

username = "khashstudioz@gmail.com"
password = "Kanimilky@21697"

# creata a imap object
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# login
result = imap.login(username, password)

# Use "[Gmail]/Sent Mails" for fetching
# mails from Sent Mails.
imap.select('"[Gmail]/All Mail"',
            readonly=True)

response, messages = imap.search(None,
                                 'UnSeen')
messages = messages[0].split()

# take it from last
latest = int(messages[-1])

# take it from start
oldest = int(messages[0])

unread_msgs = [int(i) for i in messages]
print(unread_msgs)



for i in unread_msgs:
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            # print required information
            print(msg["Date"])
            print(msg["From"])
            print(msg["Subject"])
            print(msg["Body"])



            # str_list = list(filter(None, messages[0].decode().split(' ')))
            # print('No. of messages: {}'.format(len(str_list)))
            # if retcode == 'OK':
            #     for num in messages[0].decode().split(' '):
            #         if num:
            #             typ, data = conn.fetch(num, '(RFC822)')
            #             for response_part in data:
            #                 if isinstance(response_part, tuple):
            #                     email_message = email.message_from_string(str(response_part[1]))
            #                     print(email_message)








            # def get_email_body(emailobj):
            #     """ Return the body of the email, preferably in text.
            #     """
            #
            #     def _get_body(emailobj):
            #         """ Return the first text/plain body found if the email is multipart
            #         or just the regular payload otherwise.
            #         """
            #         if emailobj.is_multipart():
            #             for payload in emailobj.get_payload():
            #                 # If the message comes with a signature it can be that this
            #                 # payload itself has multiple parts, so just return the
            #                 # first one
            #                 if payload.is_multipart():
            #                     return _get_body(payload)
            #
            #                 body = payload.get_payload()
            #                 if payload.get_content_type() == "text/plain":
            #                     return body
            #         else:
            #             return emailobj.get_payload()
            #
            #     body = _get_body(emailobj)
            #
            #     enc = emailobj["Content-Transfer-Encoding"]
            #     if enc == "base64":
            #         body = base64.decodestring(body)
            #
            #     return body







                #
            # stat, total1 = result.select('Inbox')
            # stat, data1 = result.fetch(total1[0], "(UID BODY[TEXT])")
            # msg = data1[0][1]
            # soup = BeautifulSoup(msg, "html.parser")
            # txt = soup.get_text()
            # print("Body :" + txt)
            # # result.close()
            # # result.logout()
            # print("prinnted")

    # for part in msg.walk():
    #     if part.get_content_type() == "text / plain":
    #         # get text or plain data
    #         body = part.get_payload(decode=True)
    #         print(f'Body: {body.decode("UTF-8")}', )

            # b = email.message_from_string(a)
            # if b.is_multipart():
            #     for payload in b.get_payload():
            #         # if payload.is_multipart(): ...
            #         print()
            #         payload.get_payload()
            # else:
            #     print()
            #     b.get_payload()

    print()




# for i in range(23, 23 - 20, -1):
#     # fetch
#     res, msg = imap.fetch(str(i), "(RFC822)")
#
#     for response in msg:
#         if isinstance(response, tuple):
#             msg = email.message_from_bytes(response[1])
#             # print required information
#             print(msg["Date"])
#             print(msg["From"])
#             print(msg["Subject"])
#             print()
#         for part in msg.walk():
#             if part.get_content_type() == "text / plain":
#                 # get text or plain data
#                 body = part.get_payload(decode=True)
#                 print(f'Body: {body.decode("UTF-8")}', )