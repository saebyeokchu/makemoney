import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def extractTxts(source) :
    global txts
    
    
    #많은 타이틀이 news-tit아래 태그로 씌워져 있음
    tits = results.find_all("h2",class_="news-tit");

    for tit in tits:
        txt = tit.find("a").text
        txts.append(txt)

txts = []
URL = "https://www.hankyung.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#위쪽 주제들
results = soup.find("div",class_="main-top-wrap")
extractTxts(results)

#중간 메인 주제
results = soup.find("article",class_="major-thumb-news")
extractTxts(results)

results = soup.find("section",class_=["main-component","series"]);
extractTxts(results)
    
fileName = datetime.now().date()
os.makedirs(f'C:/Users/cuu22/Desktop')

fileFullPath = f'C:/Users/cuu22/Desktop/{fileName}.txt'

#txt 모아서 파일로 만들기
with open(fileFullPath, "w") as f:
    f.write("Hello world!")

    
