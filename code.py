import requests
import re

countmail=0
countLink=0
link=[]
visited=[]
link.append("https://www.example.com/")

while(len(link)>0):
    try:
        lk=link.pop()
        print(lk)
        visited.append(lk)
        data=requests.get(lk)
        text=data.text
        p=re.findall('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',text)
        for i in p:
            countmail+=1
            print(countmail, "==> ", i )

        p=re.findall('http[a-zA-Z:/]+[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,}',text)

        for i in p:
            if i not in visited and i not in link:
                countLink+=1
                #print('****',countLink, '--> ', i)
                link.append(i)
    except a:
        print('Error')
