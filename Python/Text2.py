from bs4 import BeautifulSoup
import requests
import re

# 讀取網頁
res = requests.get('https://cecilspeaks.tumblr.com/post/56680281610/episode-1-pilot')
soup = BeautifulSoup(res.text, "html.parser")

# 抓取資料
catch = soup.find('div', 'side-box ruled-top').find_all(href=re.compile("/ep"))

# 讀入連結
file = open( './Links.txt', 'w', encoding='UTF-8')
for i in range(len(catch)):
    link = catch[i].get('href')
    file.write('https://cecilspeaks.tumblr.com'+link)
    file.write("\n")
file.close()

# 讀入標題
file = open( './Title.txt', 'w', encoding='UTF-8')
for i in range(len(catch)):
    title = catch[i].get_text().replace('/', '').replace('?', '').replace(':', '').replace('"', '').replace('\'', '')
    file.write(title)
    file.write("\n")
file.close()