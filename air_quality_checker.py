#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import datetime
url = 'https://aqicn.org/city/usa/minnesota/minneapolis-near-road/'


#print(help(request=requests))

page = requests.get(url)

s = BeautifulSoup(page.content, 'html.parser')

data = s.find(id="aqiwgtvalue")
status = s.find(id="aqiwgtinfo")


with open('/Users/nuremo/Desktop/projects/Air_Quality_Tracker/air_record.txt', 'a') as f:
    f.write(f"Air Quality {status.text}: {data.text} {str(datetime.datetime.now())} \n")
