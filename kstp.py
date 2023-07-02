import requests
from bs4 import BeautifulSoup
import os
from twilio.rest import Client





##### WILL RUN AN ERROR IF THERE ARE NO NEWS AND IT IS RUN ####





account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
my_number = os.environ.get('my_number')
twilio_number = os.environ.get('my_twilio_number')


url = "https://kstp.com/kstp-news/local-news/"
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')
#print(s.title.string)
words_to_watch = ["police","emergency","gunshots","severe","fire","murder","tornado","wreckage","crash","killed","injured","dies","shooting","hurt","dead","drunk","crash","terrorized","severe"]


new_headlines_for_the_day = []

def past_news(some_text):
    with open("work.txt", 'r') as f:
        reading = f.readlines()
        for i in reading:
            #print (some_text.strip() + "   " + i)
            if str(some_text).strip() == i.strip():
                return True
        return False

job_title = s.find_all(class_="col-12 col-lg-9 hbi2020-archive-block")

new_new = " "
def check_news():
    for i in job_title:
        i = i.text
        #print (i)
        w = i.split('\n')
        w = ' '.join(w)
        w = w.split('       ')
      
        for r in w:
            r = r.strip()
            new_headlines_for_the_day.append(r)
            #print ("Looking: "+r)
            if past_news(r):
                pass
            else:
                global new_new; new_new = r
                return False


if check_news() == False:
    print ("adding to file: " + new_new)
    with open("work.txt", 'a') as f:
            f.write(new_new)
            f.write('\n')


new_headlines_for_the_day = []


client = Client(account_sid, auth_token)

if new_new == " ":
    pass
else:
    client.messages.create(
            to = my_number,
            from_ = twilio_number,
        # max char Twilio can send: 72
            body = new_new[0:72]
        )


#for writing to files: 
# with open("work.txt", 'w') as f:
#     for i in new_headlines_for_the_day:
#         f.write(i)
#         f.write('\n')


