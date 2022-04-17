'''Sending emails with Python'''
import ssl
import smtplib
from email.message import EmailMessage

def main():

    subject = "Email coming from python"
    body = "This is a test email sent by my Python code"
    sender_email = "renata.kyriakatou@gmail.com"
    receiver_email = "kkyriakatos@gmail.com"

    password = input("Enter a password: ")

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    context = ssl.create_default_context()

    print("Sending email!")

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,message.as_string())
    print("Successful sending of email!")


#Main Call to main()
if __name__ == '__main__':
    main()
