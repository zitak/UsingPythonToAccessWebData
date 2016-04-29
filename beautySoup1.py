import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')

count = 0
sum = 0
for tag in tags:
    count += 1
    num = tag.contents[0]
    sum += int(num)

print('Count ', count)
print('Sum ', sum)
