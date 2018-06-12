import re
import requests
from bs4 import BeautifulSoup

url = '***************'
r = requests.get(url)
print (r)