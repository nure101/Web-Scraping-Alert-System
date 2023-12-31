import os
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

# pritvate Twilio acct
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')

#keep private 

client = Client(account_sid, auth_token)

client.messages.create(
        #keep private 
        to = "+",
        from_ = "+",
    # max char Twilio can send: 72
        body = title
    )
