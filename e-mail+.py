from operator import le
import os
import smtplib
from email.message import EmailMessage
from senha import senha


e = input('Ensira o e-mail alvo: ')





try:
        x = int(input('Ensira a quantidade de e-mails: '))
except:
        print("Ponha apenas numeros! ")
        try:
                 x = int(input('Ensira a quantidade de e-mails: '))
        except:
                print("Ponha apenas numeros! ")







print('Carregando...')
from tqdm import tqdm 
import time
with tqdm(total=100) as pbar:
    for i in range(7):
        time.sleep(1.5)
        pbar.update(10)
        pbar.update(5)

print('Aguarde um instante! ')

for i in range(x):
    EMAIL_ADDRESS = e
    EMAIL_PASSWORD = senha
    msg = EmailMessage()
    msg['Subject'] = 'Tua mãe é uma gorda'
    msg['From'] = e
    msg['To'] = e
    msg.set_content('Testando minha automação de enviar e-mail')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


print('E-mails enviados!')
