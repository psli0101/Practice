import requests
from bs4 import BeautifulSoup

url = '***************'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

file = 0
for allfind in soup.find_all('img', alt = 'image'):
    print(allfind['data-src'])
    r = requests.get(allfind['data-src'])
    f = open('str'+str(file)+'.jpg', 'wb')
    f.write(r.content)
    file = file + 1
