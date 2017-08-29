import requests
from bs4 import BeautifulSoup

r = requests.get("https://ck101.com/thread-1319263-1-143.html")
print(r.text)

soup = BeautifulSoup(r,'html.parser')
print(soup)

tmp = soup.find_all('td','t_f')
for x in tmp:
	print(x)