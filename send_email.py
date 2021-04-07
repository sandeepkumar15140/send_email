import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = "Sarthak Enterprises"
email['to']  = "@gmail.com" #email address to who you want to send the email
email['subject'] = "Sarthak Enterprises welcomes you!"

email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('@gmail.com', 'your password')   #include email address from which you want to send an email
    smtp.send_message(email)
    print('all good boss!')