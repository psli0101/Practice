from bs4 import BeautifulSoup
import requests
import re

# 讀取Links文件
file = open('Links.txt', 'r')
result_link = list()
for line in open('Links.txt'): 
    line = file.readline().replace('\n', '')
    result_link.append(line)
print (result_link)
file.close()

file = open('Title.txt', 'r')
result_title = list()
for line in open('Title.txt'): 
    line = file.readline().replace('\n', '')
    result_title.append(line)
print (result_title)
file.close()

for i in range(len(result_link)):
    # 讀取網頁
    res = requests.get(result_link[i])
    soup = BeautifulSoup(res.text, "html.parser")

    # 找到標題
    #txt_name = soup.find('h2', 'post-title').get_text()

    # 寫入TXT
    file = open( './******/'+result_title[i]+'.txt', 'w', encoding='UTF-8')
    file.write('TITLE：'+result_title[i]+'\n\n\n')
    for str in soup.find_all('p'):
        if str.get_text() == "Audio available at: nightvale.libsyn.com" :
            break
        else:
            file.write(str.get_text())
            file.write("\n\n")
    file.close()
