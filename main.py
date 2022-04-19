from gtts import gTTS
import os
from playsound import playsound
import speech_recognition as sr
import pyttsx3
import smtplib

MY_EMAIL = "khashstudioz@gmail.com"
MY_PASSWORD = "Kanimilky@21697"

r = sr.Recognizer()

def texttospeech(text):
    language = 'en'

    myobj = gTTS(text=text, lang=language, slow=False)

    myobj.save("welcome.mp3")

    playsound("welcome.mp3")
    # os.remove("welcome.mp3")


def speechtotext(dur = 5):
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=dur)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)
        # texttospeech("Did you just said "+text)
        return text

def send_mail(rec_mail, sub, body):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:                     # 587 is default mail submission port
        connection.starttls()                       # securing our connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        try:
            connection.sendmail(
                from_addr = MY_EMAIL,
                to_addrs= rec_mail,
                msg=f"Subject: {sub}\n\n{body}.",
            )
            print("mail sent")
        except smtplib.SMTPRecipientsRefused:
            i=1
            while i:
                texttospeech("you've entered wrong receiver mail address.")
                texttospeech("To try again say continue else say quit")
                decision = speechtotext()
                if decision == "quit":
                    texttospeech("Thanks for using")
                    i=0
                    return
                elif decision == "continue":
                    return voicebasedforblind()




def voicebasedforblind():
    # print("Welcome to voice based email for blind!")
    # mytext = 'Welcome to voice based email for blind'
    # texttospeech(mytext)
    # print("To whom do you want to send an email?")
    # texttospeech("To whom do you want to send an email?")
    # rec_email = speechtotext().lower()
    # rec_email = rec_email.replace(" ","")
    # rec_email = rec_email.replace("attherate", "@")
    rec_email="khashstudiozgmail.com"
    print(rec_email)


    # texttospeech("please enter the subject of the mail?")
    # subject = speechtotext()
    subject = "subject"
    print(subject)


    # texttospeech("please enter the body of the mail?")
    # body = speechtotext(dur=10)
    body="this is the body of the mail"
    print(body)

    # texttospeech("please confirm before sending the mail")
    # texttospeech("receiver mail is ")
    # texttospeech(rec_email)
    # texttospeech("subject of mail is ")
    # texttospeech(subject)

    texttospeech("body of mail is ")
    texttospeech(body)
    i=1
    while i:
        texttospeech("Say yes to continue sending the mail else say no to re enter details")
        confirmation = speechtotext()
        if confirmation == "yes":
            send_mail(rec_email, subject, body)
            return
        elif confirmation == "no":
            return voicebasedforblind()
        elif confirmation == "quit":
            texttospeech("Thanks for using")
            i=0
            return
        # elif len(confirmation)==0:                                                                                    # buggg buggg buggg
        #     texttospeech("please say the correct key word")
        else:
            texttospeech("Sorry, I didn't understand what you said, Please say again.")


#
# def main():
#     print("Welcome to voice based email for blind!")
#     mytext = 'Welcome to voice based email for blind'
#     texttospeech(mytext)
#     i=1
#     while i:
#         choices = "say send mail if you wanna send an email else say read mail if you wanna read an email"
#         texttospeech(choices)
#         ch = speechtotext().lower()
#         if ch == "send mail":
#             return voicebasedforblind()
#         elif ch=="read mail":
#             pass
#         elif ch == "exit":
#             texttospeech("Thanks for using")
#             i=0
#             return
#
#
#
#
#
# main()

voicebasedforblind()