# webscrape past login #webscrape login
# Login to website using just Python 3 Standard Library
import urllib.parse
import urllib.request
import http.cookiejar
import webbrowser
import bs4
from urllib.request import urlopen as uReq, Request
from bs4 import BeautifulSoup as soup
import time


import mechanize
from bs4 import BeautifulSoup
import http.cookiejar
a = True
while a == True:
    cj = http.cookiejar.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("https://powerschool.whps.org/public/home.html")

    br.select_form(nr=0)
    br.form['account'] = '118358'
    br.form['pw'] = 'Frankie'
    br.submit()

    html = str(br.response().read())
    print(html)
    if '88.9' not in html:
        a = False
        print('nice')
        webbrowser.open("https://www.youtube.com/watch?v=dvgZkm1xWPE")
        time.sleep(10)
        webbrowser.open("https://powerschool.whps.org/public/home.html")
    print('test')

#print(row)
#row.findAll("tr",{"id":"ccid_1463352"})

#website = f'https://www.reddit.com/top' # gets that subreddits front page
#hdr = {'User-Agent': 'Mozilla/5.0'}# this stuff
#req = Request(website,headers=hdr)# makes it so I can use any website
#UClient = uReq(req)
#page_html = UClient.read()
#UClient.close()
#page_soup = soup(page_html, "html.parser")

#value = page_soup.findAll("a",{"class":"_3ryJoIoycVkA88fy40qNJc"})