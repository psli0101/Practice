from bs4 import BeautifulSoup
import requests
import re

# 讀取網頁
res = requests.get('https://cecilspeaks.tumblr.com/post/56680281610/episode-1-pilot')
soup = BeautifulSoup(res.text, "html.parser")

# 找到標題
txt_name = soup.find('h2', 'post-title').get_text()

# 寫入TXT
file = open( './'+txt_name+'.txt', 'w', encoding='UTF-8')
file.write(soup.find('p').get_text())
file.close()