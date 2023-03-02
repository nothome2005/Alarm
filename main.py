from twilio.rest import Client
import os
from urllib.request import urlopen
import json


SID = os.getenv('SID')
auth = os.getenv('auth')

cl = Client(SID,auth)

def get_state():
    with urlopen('https://sirens.in.ua/api/v1/', timeout=10) as response:
        data = response.read()
        return json.loads(data)['Kyiv City']

if __name__ == '__main__':
    with open('alarm.txt','r') as f:
        alarm = f.read()
    if get_state() != None and alarm == 'false':
        cl.messages.create(body='Увага! Тривога у Києві!',from_='+13156022921',to='+380994827097')
        alarm = 'true'
    else:
        print(get_state())
        alarm = 'false'
    with open('alarm.txt','w') as f:
        f.write(alarm)
