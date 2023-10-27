import webbrowser
import pyautogui
import bs4
from urllib.request import urlopen as uReq, Request
from bs4 import BeautifulSoup as soup

win = False

while win == False:
    pyautogui.hotkey('command','w')
    website = 'https://www.freebirthdatelottery.com/emoji-game-instantly-win-10/' # gets that subreddits front page
    webbrowser.open(website)
    hdr = {'User-Agent': 'Mozilla/5.0'}# this stuff
    req = Request(website,headers=hdr)# makes it so I can use any website
    UClient = uReq(req)
    page_html = UClient.read()
    UClient.close()
    page_soup = soup(page_html, "html.parser")
    value = page_soup.find("div",{"class":"g g-8"}).div.a.img.get('alt')
    value2 = page_soup.find("div",{"class":"g g-8"}).div.a.get('href')
    if value != 'Lose':
        win = True
        #webbrowser.open(value)
    
    print(value)