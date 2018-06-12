import re
import requests
from bs4 import BeautifulSoup

url = '**************'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

pic = soup.find('img', 'GalleryImage_image_1I6fi')
rr = requests.get(pic['src'])
print(rr.content)