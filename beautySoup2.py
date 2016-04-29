import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
for i in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[17].get('href', None)
print url

