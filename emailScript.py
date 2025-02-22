
from datetime import datetime, time, timedelta, date
import smtplib, ssl

# SMTP essentially provides functions for connecting
# and sending emails using a Simple Mail Transfer Protocol
# Notes:
#   It can send it to any machine on the internet with a listner daemon
#   listener daemon monitors a specified datacomm port for any incoming connecting requests
from email.mime.text import MIMEText
# it provides classes for constructing and parsing email message
# (To;From;Subject; etc.) and allows
# encoding and decoding emails with the MIME
# (Multipurpose internet Mail extensions) standard.

from getpass import getpass
# used to get passwords without turning your password into plain text

# app gmail password
password = input("Input your password: ")
#email contacts
sender= "testwxray@gmail.com"
recipients = "testwxray@gmail.com"
# SMTP server address, port
smtp_server = "smtp.gmail.com"
port = 465
#meta data
subject = "test subject"
body = "body of text message"

#TODO creating a function to assemble all email components

def email_new(g_sender, g_recipients, g_subject, g_body, g_password):
  # lists off headings for the email in order they are inserted into the list
  e_msg = MIMEText(g_body) # creates message containing text
  e_msg['Subject'] = g_subject
  e_msg['To'] = g_recipients
  e_msg['From'] = g_sender
  # creates the connection between the program and the gmail account
  context = ssl.create_default_context()
  try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      # login for the SMTP server is the users gmail account
      server.login(g_sender, g_password)
      # sendmail method sends the message inside the SMTP server
      server.sendmail(g_sender, g_recipients, e_msg.as_string())
      print("message")
  except Exception as e:
    print(f" Exception: {e}")


email_new(sender, recipients, subject, body, password)
#In both instances, Gmail will encrypt
# emails using TLS, as this is the more
# secure successor of SSL. As per Python’s
# Security considerations, it is highly
# recommended that you use
# create_default_context() from the ssl
# module.








