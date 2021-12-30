#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.
# Preset values:
import credentials.py as credentials

accountSID = credentials.accountSID
authToken  = credentials.authToken

myNumber = '+918921996073'
twilioNumber = '+16204904375'
from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

textmyself('The boring task is finished.')