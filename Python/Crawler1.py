import requests
from bs4 import BeautifulSoup

tmp = requests.get("https://ck101.com/thread-1319263-1-143.html")
print(tmp.text)