import requests
from bs4 import BeautifulSoup
import operator

url_rq = "http://knit.ac.in/coe/ODD_2016/btreg16xcdaz.asp?rollno="
dic = {}
roll=[]
k=(input("Enter the branch code"))
regsr=int('15'+k+'01')
reger=int('15'+k+'70')
latsr=int('168'+k+'01')
later=int('168'+k+'30')




for i in range(regsr, reger):
    roll.append(i)
for i in range(latsr,later):
    roll.append(i)

for i in roll:
    try:
        url = url_rq + str(i)
        print(url)
        response = requests.get(url)
        res_text = response.text
        soup = BeautifulSoup(res_text,"html.parser")
        li = []
        for link in soup.find_all('td'):
            st = str(link.string)
            li.append(st)
        for j in range(0, len(li)):
            if li[j] =="Name:":
                k = li[j+1]
            elif li[j] == "Second Year":
                l = li[j+1]

        m=""
        for z in l:
            if z=='/':
                break
            else:
                m = m+z
        number = int(m)
        dic[k] = number
    except:
        continue
a1_sorted = sorted(dic, key=dic.get, reverse=True)
c = 1
for i in a1_sorted:
    print(c, "=>", i, ": ", dic[i])
    c = c + 1
