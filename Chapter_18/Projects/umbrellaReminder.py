
#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import requests
import json
import credentials
from twilio.rest import Client

accountSID = credentials.accountSID
authToken  = credentials.authToken

myNumber = '+918921996073'
twilioNumber = '+16204904375'

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

list =[200,210,202,211,212,221,230,231,232,300,301,302,310,311,312,313,314,321,500,501,502,503,504,511,520,521,522,531]

APPID = '055d63a4c7cec39dbe8497a6c249b78d'
location = 'palakkad'

url ='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(location,APPID)

response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)
if weatherData['weather'][0]['id'] in list:
    weather = weatherData['weather'][0]['weather']
    textmyself('It will be {} today. Please carry your umbrella'.format(weather))

