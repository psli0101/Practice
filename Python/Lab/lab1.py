import re
import requests
from bs4 import BeautifulSoup

url = '***********'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'}
r = requests.get(url, headers = headers)
print (r)