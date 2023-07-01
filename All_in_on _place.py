from twilio.rest import Client
import requests
from bs4 import BeautifulSoup




print("Checking news...")

# custmize the url so you can check multi local news stations 
url = "https://www.fox9.com/news/minneapolis-police-investigate-fatal-shooting-at-20th-and-chicago-ave" 
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

# we don't want to read the whole article. articles usually include time and date, event that took place, and casualties. So we only really need
# the title 
title = s.title.string
print(title)

# pritvate Twilio acct # don't share
account_sid = "AC46cc7d05ca5e70df445c8ce1115a7ff9"
auth_token = "8f8543d1b249f4e4f58f1c324451e650"

client = Client(account_sid, auth_token)

client.messages.create(
        to = "+16124537222",
        from_ = "+18339413795",
    # max char Twilio can send: 72
        body = title
    )
