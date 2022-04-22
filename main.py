from decouple import config

from gtts import gTTS
import os
from playsound import playsound
import speech_recognition as sr
import pyttsx3
import smtplib
import imaplib
import email
from imaplib import IMAP4 as IMAP



# from ui import blind_mail_interface
from imap_tools import MailBox, MailMessageFlags, A



""" Beep sound """
from pygame import mixer
mixer.init()
sound = mixer.Sound("beep.mp3")
# sound.play()



MY_EMAIL = config('EMAIL')
MY_PASSWORD = config('SECURITY_KEY')

r = sr.Recognizer()

class email_sys:

    def intro(self):
        self.texttospeech("thankyou for coming to this section")
        self.texttospeech("before proceeding please remember the following 4 rules")
        self.texttospeech("1 always speak after beep sound")
        self.texttospeech("2 you can exit from anywhere by saying exit or quit")
        self.texttospeech("3 while searching mails of a particular user use their email id")
        self.texttospeech("4 if you have more than 1 unseen mails, you will be listening mails from newest to oldest")


    def texttospeech(self,text):
        language = 'en'

        myobj = gTTS(text=text, lang=language, slow=False)

        myobj.save("welcome.mp3")

        playsound("welcome.mp3")
        # os.remove("welcome.mp3")


    def speechtotext(self, dur = 5):
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            self.audio_data = r.record(source, duration=dur)
            print("Recognizing...")
            # convert speech to text
            self.text = r.recognize_google(self.audio_data)
            print(self.text)
            # texttospeech("Did you just said "+text)
            return self.text


    def particular_users_mail(self,newest_to_oldest, result):
        """ error in this part """
        try:
            self.texttospeech("enter mail of the user to fetch their new mails")
            self.user = self.speechtoxt().lower()
            self.user = self.user.replace(" ", "")
            self.user = self.user.replace("attherate", "@")
            # self.user = "khashstudioz@gmail.com"
            self.user1 = '<'+self.user+">"

            print(self.user1)
            # self.texttospeech(f"fetching mails of {self.user}")
        except:
            print("error")
            pass
        z=[]
        for i in range(len(newest_to_oldest)):
            print(f"Mail {i+1}")
            res, msg = self.imap.fetch(str(newest_to_oldest[i]), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    self.msg = email.message_from_bytes(response[1])
                    # print("before if", self.msg)
                    print(self.user in self.msg["From"].split())

                    bIsUid = False


                    if self.msg["From"] == self.user or self.msg["From"] == self.user1:
                        print("after if")
                        z.append(newest_to_oldest[i])
                        # flags = (MailMessageFlags.ANSWERED, MailMessageFlags.FLAGGED)
                        # self.imap.flag(self.imap.uids(A(seen=False)), flags, True)
                        print(id)
                        # ID = (id).to_bytes(2, byteorder='big')
                        # IMAP.store(id, "0", "\Seen")
                        result.uid('STORE',id,'+FLAGS','(\\Seen)')
                    else:
                        # IMAP.store(id, "0", "\Seen")
                        result.uid('STORE', id, '+FLAGS', '(\\Seen)')
        self.texttospeech(f"you have {len(z)} unseen mails from this user")
        print("z: ",z)
        # self.receive_unseen_mail(z)


    def receive_unseen_mail(self, newest_to_oldest):
        print()
        print("*****---------- receive mail ----------*****")

        self.texttospeech("A quick disclaimer you will be listening mails from newest to oldest")
        print("_____Disclaimer______")
        print(newest_to_oldest)
        for i in range(len(self.newest_to_oldest)):
            self.texttospeech(f"Mail {i+1}")
            self.res, self.msg = self.imap.fetch(str(self.newest_to_oldest[i]), "(RFC822)")
            for response in self.msg:
                if isinstance(response, tuple):
                    self.msg = email.message_from_bytes(response[1])
                    self.email_date = self.msg["Date"]
                    self.email_from = self.msg["From"]
                    self.email_subject = self.msg["Subject"]

            for part in self.msg.walk():
                if part.get_content_type() == "text/plain":
                    # get text or plain data
                    self.body = part.get_payload(decode=True)
                    self.mail_body = self.body.decode("UTF-8")
                    print(f"Date : {self.email_date}")
                    print(f"From : {self.email_from}")
                    print(f"Subject : {self.email_subject}")
                    print(f'Body: {self.mail_body}', )
                    self.texttospeech(f"you receive this mail from {self.msg['From']} at {self.msg['Date'][:16]} with subject {self.msg['Subject']} and body is {self.mail_body}")

            print("............................................................")

    def read_mail(self):

        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        result = self.imap.login(MY_EMAIL, MY_PASSWORD)

        # Use "[Gmail]/Sent Mails" for fetching mails from Sent Mails.
        self.imap.select('inbox', readonly=True)
        response, messages = self.imap.search(None, 'UnSeen')
        # print(response, messages)
        self.messages = messages[0].split()

        self.unread_msgs = [int(i) for i in self.messages]
        self.newest_to_oldest = self.unread_msgs[::-1]
        # print(newest_to_oldest)
        print("unread msgs : ", len(self.unread_msgs))

        if len(self.unread_msgs) == 0:
            self.texttospeech("You have no new mail, please come back after some time")

        else:
            self.texttospeech(f"You have {len(self.unread_msgs)} new mails")
            i=True
            while i:
                try:
                    self.texttospeech("To listen all of them say all mail or to listen mail from a particular user say get mail")
                    print("To listen all of them say all mail or to listen mail from a particular user say get mail")

                    ch = self.speechtotext().lower()
                    # ch="get mail"
                    if ch == "all mail" or ch=="all the mails" or ch=="all mails":
                        i=False
                        self.receive_unseen_mail(self.newest_to_oldest)
                    elif ch =="get mail" or ch=="getmale" or ch == "get the mail" or "get mails":
                        i=False
                        self.particular_users_mail(self.newest_to_oldest, result)
                    elif ch == "quit" or ch=="exit":
                        self.texttospeech("Thanks for using")
                        i=False
                        break
                    else:
                        self.texttospeech("Sorry, I didn't recognise what you said, Please say again.")

                except sr.UnknownValueError:
                    self.texttospeech("Sorry, I didn't recognise what you said, Please say again.")


    def send_mail(self, rec_mail, sub, body):
        print()
        print("*****---------- sending mail ----------*****")
        # self.texttospeech("Mail sent successfully")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:                     # 587 is default mail submission port
            connection.starttls()                       # securing our connection
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            try:
                connection.sendmail(
                    from_addr = MY_EMAIL,
                    to_addrs= rec_mail,
                    msg=f"Subject: {sub}\n\n{body}.",
                )
                return self.texttospeech("Mail sent successfully to "+str(rec_mail))
            except smtplib.SMTPRecipientsRefused:
                i=True
                while i:
                    try:
                        self.texttospeech("you've entered wrong receiver mail address.")
                        self.texttospeech("To try again say continue else say quit")
                        mixer.Sound("beep.mp3").play()
                        decision = self.speechtotext()
                        if decision == "quit":
                            self.texttospeech("Thanks for using")
                            i=False

                        elif decision == "continue":
                            i=False
                            self.voicebasedforblind()
                        else:
                            self.texttospeech("Sorry, I didn't recognise what you said, Please say again.")
                    except sr.UnknownValueError:
                        self.texttospeech("Sorry, I didn't recognise what you said, Please say again.")


    def voicebasedforblind(self):
        print()
        print("*****---------- voicebasedforblind ----------*****")
        try:
            print("To whom do you want to send an email?")

            self.texttospeech("To whom do you want to send an email?")
            mixer.Sound("beep.mp3").play()
            self.rec_email = self.speechtotext(dur=8).lower()
            self.rec_email = self.rec_email.replace(" ","")
            self.rec_email = self.rec_email.replace("attherate", "@")
            # self.rec_email="burmakanishka@.com"
            print(self.rec_email)
            self.texttospeech("please enter the subject of the mail?")
            mixer.Sound("beep.mp3").play()
            self.subject = self.speechtotext(dur=8)
            # self.subject = "subject"
            print(self.subject)
            self.texttospeech("please enter the body of the mail?")
            mixer.Sound("beep.mp3").play()
            self.body = self.speechtotext(dur=10)
            # self.body="this is the body of the mail"
            print(self.body)
        except sr.UnknownValueError:
            self.texttospeech("please do not leave any field empty")
            self.voicebasedforblind()
        else:
            self.texttospeech("please confirm before sending the mail")
            self.texttospeech("receiver mail is ")
            self.texttospeech(self.rec_email)
            self.texttospeech("subject of mail is ")
            self.texttospeech(self.subject)

            self.texttospeech("body of mail is ")
            self.texttospeech(self.body)
        i = True
        # k = 0
        while i:
            try:
                self.texttospeech("Say yes to continue sending the mail else say no to re enter details")
                mixer.Sound("beep.mp3").play()
                self.confirmation = self.speechtotext()
                if self.confirmation == "yes":
                    i=False
                    self.send_mail(self.rec_email, self.subject, self.body)

                elif self.confirmation == "no":
                    self.voicebasedforblind()
                    break

                elif self.confirmation == "quit":
                    i=False
                    self.texttospeech("Thanks for using")

                else:
                    self.texttospeech("Sorry, I didn't recognise what you said, Please say again.")
            except:
                self.texttospeech("Sorry, I didn't recognise what you said, Please say again.")



    def main_file(self):
        print()
        print("*****---------- menu ----------*****")
        print("Welcome to voice based email for blind!")
        mytext = 'Welcome to voice based email for blind'
        self.texttospeech(mytext)
        i=True
        while i:
            try:
                choices = "say introduction if you are a new user or say send mail if you wanna send an email"
                self.texttospeech("say introduction if you are a new user or say send mail if you wanna send an email")
                self.texttospeech(" or say read mail if you wanna read an email")
                mixer.Sound("beep.mp3").play()
                ch = self.speechtotext().lower()
                # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                # ch = "read mail"
                if ch == "send mail" or ch == "send a mail":
                    self.voicebasedforblind()

                elif ch=="read mail" or ch == "read my mails":
                    self.read_mail()
                elif ch == "exit":
                    self.texttospeech("Thanks for using")
                    i=False
                elif ch == "introduction":
                    self.intro()
                else:
                    self.texttospeech("Sorry, I didn't recognise what you said, Please say again.")

            except sr.UnknownValueError:
                self.texttospeech("Sorry, I didn't recognise what you said, Please say again.")


# main()
q = email_sys().main_file()