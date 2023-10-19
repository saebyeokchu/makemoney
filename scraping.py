import requests
from bs4 import BeautifulSoup

URL = "https://www.hankyung.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#위쪽 주제들
results = soup.find("div",class_="main-top-wrap")

#많은 타이틀이 news-tit아래 태그로 씌워져 있음
tits = results.find_all("h2",class_="news-tit");

for tit in tits:
    txt = tit.find("a").text
    print(txt)
