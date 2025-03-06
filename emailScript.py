# time modules
from datetime import datetime, timedelta
from pickle import FALSE
from time import time, sleep
import pytz

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

# used to get passwords without turning your password into plain text
# app gmail password rvhq cumf hhtr yxuq
password = input("Input your app password: ")

# Email contacts
def email_info():
  sender_info = "testwxray@gmail.com"
  recipients_info = "testwxray@gmail.com"
  # SMTP server address, port for google account
  smtp_server_info = "smtp.gmail.com"
  port_info = 465
  # meta data
  subject_info = "test subject"
  body_info = "body of text message"
  return sender_info, recipients_info, smtp_server_info, port_info, subject_info, body_info

# Set_date sets the date the email will be sent
# Input from user for date year, month, and day
def input_date_time():
  time_type_condition = True
  set_time_type_input = ""
  set_date_input = input("input date in format(YYYY-MM-DD): ")
  set_time_input = input("input time in format(HH:MM:SS): ")
  #Validate date input is in correct format or values
  try:
    datetime.strptime(set_date_input, "%Y-%m-%d")
    datetime.strptime(set_time_input, "%H:%M:%S")
  except ValueError:
    print(f"ValueError incorrect value usage")
  # while time_type_condition == True
  # validates time_type input to be pm or am
  while time_type_condition:
    set_time_type_input = input("input time type (pm and am): ").lower()
    print(set_time_type_input)
    if set_time_type_input == "pm" or set_time_type_input == "am":
      print(f"valid {set_time_type_input}")
    else:
      print(f"invalid {set_time_type_input} input am or pm")
  return set_time_input, set_date_input, set_time_type_input

def convert_time(user_time,user_date,time_type):
  convert_set_time_string = ""
  if time_type == "am":
    pass
  elif time_type == "pm":
    user_time_list = user_time.split(":")
    print(user_time_list[0])
    user_time_list[0] = int(user_time_list[0]) + 12
    for i in range(0,len(user_time_list)):
      if i == 0:
        convert_set_time_string = convert_set_time_string + str(user_time_list[i])
      else:
        convert_set_time_string = convert_set_time_string +":"+ str(user_time_list[i])
  else:
    print("invalid time type")
    return -1
  return user_date + " " + convert_set_time_string
# email_new a function to assemble all email components
def email_new(g_sender, g_recipients, g_subject, g_body, g_password):
  # lists off headings for the email in order they are inserted into the list
  e_msg = MIMEText(g_body) # creates message containing text
  e_msg['Subject'] = g_subject
  e_msg['To'] = g_recipients
  e_msg['From'] = g_sender
  # creates the connection between the program and the gmail account
  context = ssl.create_default_context()
  # Checks if the connection between Google Gmail SMTP server
  try:
    #starts the connection with the smtp_server for gmail
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      # login for the SMTP server is the users gmail account
      server.login(g_sender, g_password)
      # sendmail method sends the message inside the SMTP server
      server.sendmail(g_sender, g_recipients, e_msg.as_string())
      print("message")
  except Exception as e:
    print(f" Exception: {e}")

def email_condition(formated_date_time_conditional):
  while True:
    # sleep(1) pauses the execution for one second
    sleep(1)
    # Todo convert timezone into usable comparison format(complete)
    # timezone_date gets the date and time within the timezone
    # timezone_time_string converts the timezone into a string
    # timezone_time_string_format grabs only the date and time (excluding miliseconds and actual time)
    # making it comparable to the users input
    timezone_time = datetime.now(pytz.timezone('US/Central'))
    timezone_time_string = str(timezone_time)
    timezone_time_string_formated = timezone_time_string[:19]
    print(f"time zone time: {timezone_time_string_formated}")
    print(formated_date_time_conditional)
    if timezone_time_string_formated == formated_date_time_conditional:
      email_new(sender, recipients, subject, body, password)
      break
    # email_new(sender, recipients, subject, body, password)
    # In both instances, Gmail will encrypt
    # emails using TLS, as this is the more
    # secure successor of SSL. As per Python’s
    # Security considerations, it is highly
    # recommended that you use
    # create_default_context() from the ssl
    # module.

sender, recipients, smtp_server, port, subject, body = email_info()
set_time,set_date,set_time_type = input_date_time()
formated_set_date_time = convert_time(set_time,set_date, set_time_type)
print(f"date and time: {datetime.now(pytz.timezone('US/Central'))}  formated_set_date_time: {formated_set_date_time}")
email_condition(formated_set_date_time)






