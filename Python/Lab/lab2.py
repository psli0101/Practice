import re
import requests
from bs4 import BeautifulSoup

url = '*************'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; ***************'}
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'html.parser')
rr = soup.find('table', id = re.compile('pid')).find('td', id = re.compile('postmessage_'))
rrr = soup.find("td",attrs={"class":"t_f"})
print(rrr.text)
