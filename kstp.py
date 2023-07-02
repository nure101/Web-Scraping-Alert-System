
import requests
from bs4 import BeautifulSoup




url = "https://kstp.com/kstp-news/local-news/"
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')
#print(s.title.string)
words_to_watch = ["emergency","gunshots","severe","fire","murder","tornado","wreckage","crash","killed","injured","dies","shooting","hurt","dead","drunk","crash","terrorized","severe"]


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
            r = "wellll"
            new_headlines_for_the_day.append(r)
            #print ("Looking: "+r)
            if past_news(r):
                return True
            else:
                global new_new; new_new = r
                return False


if check_news() == False:
    print ("adding to file: " + new_new)
    with open("work.txt", 'a') as f:
            f.write(new_new)
            f.write('\n')


new_headlines_for_the_day = []


# with open("work.txt", 'w') as f:
#     for i in new_headlines_for_the_day:
#         f.write(i)
#         f.write('\n')


