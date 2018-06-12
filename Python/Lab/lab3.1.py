import re
import requests
from bs4 import BeautifulSoup

url = '*************'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

file = 0
for pic in soup.find_all('img', 'GalleryImage_image_1I6fi'):
    rr = requests.get(pic['src'])
    f = open(str(file)+'.jpg', 'wb')
    f.write(rr.content)
    file = file + 1