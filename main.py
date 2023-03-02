from twilio.rest import Client
#from urllib.error import HTTPError, URLError
from urllib.request import urlopen
import json

SID = 'AC16c5f7cd9783460a0476ff7f8e6fcbdc'
auth = '412eef4b9dc77914e1eb58ceef9be5b1'
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