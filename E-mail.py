import os
import smtplib
from email.message import EmailMessage
EMAIL_ADRESS = 'youadress@gmail.com'
EMAIL_PASSWORD = 'you password'
msg = EmailMessage()
msg['Subject'] = '> > you text here < <'
msg['From'] = 'youadress@gmail'
msg['To'] = 'youtarget@gmail'
msg.set_content('>> you text here <<')
with smtplib.SMTP_SSL('smtp.gmail.com', 465)as smtp:
  smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
  smtp.send_message(msg)
print('')
print('I think it worked :D')
print('')
