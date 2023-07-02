"https://www.cbsnews.com/minnesota/local-news/twin-cities/"
"https://www.fox9.com/"

import requests
from bs4 import BeautifulSoup 
import os
from twilio.rest import Client


account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
my_number = os.environ.get('my_number')
twilio_number = os.environ.get('my_twilio_number')

url = "https://www.fox9.com/"
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')
#print(s.title.string)
words_to_watch = ["severe","fire","murder","tornado","wreckage","crash","killed","injured","dies","shooting","hurt","dead","drunk","crash","terrorized","severe"]

happining =  set()

def what():
    job_title = s.find_all('h3')#class_="content article-list")
    check = set()
    for i in job_title:
        #find time 
        try:
            time = i.parent.parent.find('time').text
            headline = i.parent.parent.text
            time = time.split()
            if 'mins' in time and int(time[0]) < 30: #hours if needed: ('hours' in time and int(time[0]) < 5)
                for word in words_to_watch:
                    if word in i.text:
                        happining.add(headline)
        except AttributeError:
            continue
        
what()
client = Client(account_sid, auth_token)
for i in happining:
    client.messages.create(
            to = my_number,
            from_ = twilio_number,
        # max char Twilio can send: 72
            body = i[0:72]
        )
