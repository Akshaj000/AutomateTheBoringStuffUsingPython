#!python3

import random
import smtplib
import  pyinputplus as pyip

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
emails = ['abcdef@gmail.com','hijklmnop@gmail.com']
password = pyip.inputPassword("Enter passcode : ")

for emailac in emails:    
    if len(chores)>0:
        randomChore = random.choice(chores)
        chores.remove(randomChore)    
        name = emailac.split('@')
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('akshajsr000@gmail.com',password)
        smtpObj.sendmail('akshajsr000@gmail.com', emailac, 'Subject: Solong.\nDear {} , your chore is {}. Sincerely, Akshaj'.format(name[0],randomChore))
        smtpObj.quit()
    else:
        print("No more chores to assign")


