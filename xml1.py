import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)

    results = tree.findall('.//count')
    result = 0
    count = 0
    for item in results:
        count += 1
        result += int (item.text)
    print 'Count: ', count
    print 'Sum: ', result