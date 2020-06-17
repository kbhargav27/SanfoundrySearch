#first import libraries
#google
#beautyfulsoup4
#urllib3


from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import os
import webbrowser
from multiprocessing import Process

def googlesearch(text):
    links_list=[]
    for j in search(text, num=1, stop=1, pause=2):
        links_list.append(j)
    return links_list

def searchloop_sanfoundry(link,searchtext,count=0):
    if("https://www.sanfoundry.com/" in link):
        try:
            file1 = open("C:\\Users\\Krishna\\sanfoundry.txt", "w+")    #chnage file location
            response = requests.get(link)
            bs = BeautifulSoup(response.content, "html.parser")
            data = bs.find("div", {"class": "entry-content"})
            data1 = data.find_all(text=True)
            file1.write(str(data1))
            file1.close()

            links = bs.find("main", {"id": "main"}).findAll("a", attrs={
                "href": re.compile("(https://www.sanfoundry.com/)+([a-z0-9-_()])+")})
            next_pre = [links[0], links[1]]
            num = []
            for lin in next_pre:
                num.append(lin["href"])
            find = "find"
            location = "C:\\Users\\Krishna\\sanfoundry.txt"            #change file location same as above
            res = os.system(find + ' "' + searchtext + '" ' + location)
            if (res == 0):
                webbrowser.open(link, new=2)
                exit()
            else:
                if (count < 2):
                    count += 1
                    searchloop_sanfoundry(num[0], searchtext, count)
                    searchloop_sanfoundry(num[1], searchtext, count)
        except UnicodeEncodeError:
            print("not on sanfoundary")
        except AttributeError:
            print("not on sanfoundary")


def searchloop_examradar(link,searchtext,count=0):
    if("http://examradar.com/" in link):
        try:
            file2 = open("C:\\Users\\Krishna\\examradar.txt", "w+")           #chnage file location
            response = requests.get(link)
            bs = BeautifulSoup(response.content, "html.parser")
            data = bs.find("div", {"class": "entry-content clearfix"})
            data1 = data.find_all(text=True)
            file2.write(str(data1))
            file2.close()
            links_prev = bs.find("div", {"class": "mh-col-1-2 mh-post-nav-item mh-post-nav-prev"}).findAll("a", attrs={
                "href": re.compile("(http://examradar.com/)+([a-z0-9-_()])+")})
            for links in links_prev:
                prev_link = (links["href"])
            links_next = bs.find("div", {"class": "mh-col-1-2 mh-post-nav-item mh-post-nav-next"}).findAll("a", attrs={
                "href": re.compile("(http://examradar.com/)+([a-z0-9-_()])+")})
            for links in links_next:
                next_link = (links["href"])
            find = "find"
            location = "C:\\Users\\Krishna\\examradar.txt"                     #change file location same as above
            res = os.system(find + ' "' + searchtext + '" ' + location)
            if (res == 0):
                webbrowser.open(link, new=2)
                exit()
            else:
                if (count < 2):
                    count += 1
                    searchloop_examradar(next_link, searchtext, count)
                    searchloop_examradar(prev_link, searchtext, count)
        except UnicodeEncodeError:
            print("Not found in examradar")
        except AttributeError:
            print("Not found in examradar")

def searchloop_smartvidya(link,searchtext,count=0):
    if("http://www.smartvidya.co.in/" in link):
        try:

            file3 = open("C:\\Users\\Krishna\\search.txt", "w+")               #chnage file location
            response = requests.get(link)
            bs = BeautifulSoup(response.content, "html.parser")
            data = bs.find("div", {"class": "post-body entry-content"})
            data1 = data.find_all(text=True)
            file3.write(str(data1))
            file3.close()
            links_prev = bs.find("span", {"id": "blog-pager-older-link"}).findAll("a", attrs={
                "href": re.compile("http://www.smartvidya.co.in/" + "([a-z0-9-_()])+")})
            for links in links_prev:
                prev_link = (links["href"])
            links_next = bs.find("span", {"id": "blog-pager-newer-link"}).findAll("a", attrs={
                "href": re.compile("http://www.smartvidya.co.in/" + "([a-z0-9-_()])+")})
            for links in links_next:
                next_link = (links["href"])
            find = "find"
            location = "C:\\Users\\Krishna\\search.txt"            #change file location same as above
            res = os.system(find + ' "' + searchtext + '" ' + location)
            if (res == 0):
                webbrowser.open(link, new=2)
                exit()
            else:
                if (count < 2):
                    count += 1
                    searchloop_smartvidya(prev_link, searchtext, count)
                    searchloop_smartvidya(next_link, searchtext, count)
        except UnicodeEncodeError:
            print("Not found in smartvidya")
        except AttributeError:
            print("Not found in smartvidya")



def searchloop_examveda(link,searchtext):
    if("https://www.examveda.com/" in link):
        try:
            file4 = open("C:\\Users\\Krishna\\examveda.txt", "w+")                   #chnage file location
            response = requests.get(link)
            bs = BeautifulSoup(response.content, "html.parser")
            data = bs.find("div", {"class": "col-md-8"})
            data1 = data.find_all(text=True)
            file4.write(str(data1))
            file4.close()

            find = "find"
            location = "C:\\Users\\Krishna\\examveda.txt"           #change file location same as above
            res = os.system(find + ' "' + searchtext + '" ' + location)
            if (res == 0):
                webbrowser.open(link, new=2)
                exit()
        except UnicodeEncodeError:
            print("Not found in examveda")
        except AttributeError:
            print("Not found in examveda")



query=input("question: ")
google_link_sanfoundary=googlesearch(query+"sanfoundry")
google_link_examradar=googlesearch(query+"examradar")
google_link_examveda=googlesearch(query+"examveda")
google_link_smartvidya=googlesearch(query+"smartvidya")

for i in google_link_sanfoundary:
    print(i)
    Process(target=searchloop_sanfoundry(i, query)).start()
for i in google_link_examradar:
    print(i)
    Process(target=searchloop_examradar(i,query)).start()
for i in google_link_examveda:
    print(i)
    Process(target=searchloop_examveda(i,query)).start()
for i in google_link_smartvidya:
    print(i)
    Process(target=searchloop_smartvidya(i, query)).start()


