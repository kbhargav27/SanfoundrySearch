from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import os
import webbrowser

def googlesearch(text):
    links_list=[]
    for j in search(text+"sanfoundry", tld="com", num=3, stop=3, pause=2):
        links_list.append(j)
    return links_list

def searchloop(link,searchtext):
    file1 = open("abcd.txt", "w+")
    response = requests.get(link)
    bs = BeautifulSoup(response.content, "html.parser")
    data = bs.find("div", {"class": "entry-content"})
    data1 = data.find_all(text=True)
    print(data1)

    file1.write(str(data1))
    file1.close()

    links = bs.find("main", {"id": "main"}).findAll("a", attrs={
        "href": re.compile("(https://www.sanfoundry.com/)+([a-z0-9-_()])+")})
    next_pre = [links[0], links[1]]
    num=[]
    for lin in next_pre:
        num.append(lin["href"])
    print(num)


    find = "find"
    location = "C:\\Users\\Krishna\\PycharmProjects\\SanfoundrySearch\\abcd.txt"
    res = os.system(find + ' "' + searchtext + '" ' + location)
    if (res == 0):
        webbrowser.open(link, new=2)
    else:
        searchloop(num[0],searchtext)
        searchloop(num[1],searchtext)

query=input("question: ")
google_link=googlesearch(query)
print(google_link)
for i in google_link:
    searchloop(i, query)
