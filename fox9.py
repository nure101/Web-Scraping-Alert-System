"https://www.cbsnews.com/minnesota/local-news/twin-cities/"
"https://www.fox9.com/"

import requests
from bs4 import BeautifulSoup 
import datetime
from datetime import datetime



url = "https://www.fox9.com/"
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')
#print(s.title.string)
words_to_watch = ["severe","fire","murder","tornado","wreckage","crash","killed","injured","dies","shooting","hurt","dead","drunk","crash","terrorized","severe"]

curretn_date = datetime.date(datetime.now())

#returns headlines that have the above words in them 

    # def what():
    #     job_title = s.find_all('h3')#class_="content article-list")
    #     check = set()
    #     for i in job_title:
    #         i = i.text
    #         for word in words_to_watch:
    #             if word in i:
    #                 check.add(i)  
        
    #     for i in check:
    #         print (i)

    #     #return check
    # what()

# check the time 
    # print(curretn_date)
happining =  set()



    # def what():
    #     job_title = s.find_all('h3')#class_="content article-list")
    #     check = set()
    #     for i in job_title:
    #         #find time 
    #         try:
    #             time = i.parent.parent.find('time').text
    #             if 'mins' in time and int(time[0]) < 59:
    #                 happining.append(time)
        

            
            
    #         except AttributeError:
    #             continue
            
    # what()
    # print (happining)
    
#combine news headlines and time 

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

for i in happining:
    print(i)

