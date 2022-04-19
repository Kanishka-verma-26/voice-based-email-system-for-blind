import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# account credentials
username = "khashstudioz@gmail.com"
password = "Kanimilky@21697"

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)
status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 7
# total number of emails
messages = int(messages[0])

for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode(encoding)
            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            print("Subject:", subject)
            print("From:", From)
            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        print(body)
                    elif "attachment" in content_disposition:
                        # download attachment
                        filename = part.get_filename()
                        if filename:
                            folder_name = clean(subject)
                            if not os.path.isdir(folder_name):
                                # make a folder for this email (named after the subject)
                                os.mkdir(folder_name)
                            filepath = os.path.join(folder_name, filename)
                            # download attachment and save it
                            open(filepath, "wb").write(part.get_payload(decode=True))
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # print only text email parts
                    print(body)
                    print("----",body.fetch(),"----")
            if content_type == "text/html":
                # if it's HTML, create a new HTML file and open it in browser
                folder_name = clean(subject)
                if not os.path.isdir(folder_name):
                    # make a folder for this email (named after the subject)
                    os.mkdir(folder_name)
                filename = "index.html"
                filepath = os.path.join(folder_name, filename)
                # write the file
                open(filepath, "w").write(body)
                # open in the default browser
                webbrowser.open(filepath)
            print("="*100)
# close the connection and logout
imap.close()
imap.logout()




#
# import imaplib
# import email
# from email.header import decode_header
# import webbrowser
# import os
#
# username = "khashstudioz@gmail.com"
#
# password = "Kanimilky@21697"
#
# # creata a imap object
# imap = imaplib.IMAP4_SSL("imap.gmail.com")
#
# # login
# result = imap.login(username, password)
#
# # Use "[Gmail]/Sent Mails" for fetching
# # mails from Sent Mails.
# imap.select('"[Gmail]/All Mail"',
#             readonly=True)
#
# response, messages = imap.search(None,
#                                  'UnSeen')
# messages = messages[0].split()
#
# # take it from last
# latest = int(messages[-1])
#
# # take it from start
# oldest = int(messages[0])
#
# for i in range(latest, latest - 20, -1):
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
#             # print(msg["Body"])
#             print()
#
#     for part in msg.walk():
#         if part.get_content_type() == "text / plain":
#             # get text or plain data
#             body = part.get_payload(decode=True)
#             print(f'Body: {body.decode("UTF-8")}', )



#
# import imaplib
# import email
#
#
# def read_email_from_gmail():
#         mail = imaplib.IMAP4_SSL('imap.gmail.com')
#         mail.login('khashstudioz@gmail.com','Kanimilky@21697')
#         mail.select('inbox')
#
#         result, data = mail.search(None, 'ALL')
#         mail_ids = data[0]
#
#         id_list = mail_ids.split()
#         first_email_id = int(id_list[0])
#         latest_email_id = int(id_list[-1])
#
#         for i in range(latest_email_id,first_email_id, -1):
#             # need str(i)
#             result, data = mail.fetch(str(i), '(RFC822)' )
#
#             for response_part in data:
#                 if isinstance(response_part, tuple):
#                     # from_bytes, not from_string
#                     msg = email.message_from_bytes(response_part[1])
#                     print(msg)
#                     email_subject = msg['subject']
#                     email_from = msg['from']
#                     # print ('From : ' + email_from + '\n')
#                     # print ('Subject : ' + email_subject + '\n')
#                     print()
#                     print()
#
# # nothing to print here
# read_email_from_gmail()