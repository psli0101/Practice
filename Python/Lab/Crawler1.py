import re
import requests
from bs4 import BeautifulSoup

url = '*************'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; ***********'}
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'html.parser')
for rr in soup.find_all('table', id = re.compile('pid')):
	txt = rr.find('td', id = re.compile('postmessage_'))
	print(txt.text)