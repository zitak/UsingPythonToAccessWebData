import urllib
import json

#url = raw_input('Enter location: ')
url = 'http://python-data.dr-chuck.net/comments_259109.json'
if len(url) >= 1:

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data), 'characters'
    #print data
    count = 0
    sum = 0

    info = json.loads(data)
    for item in info["comments"]:
        sum += 1
        num = item["count"]
        count += num

    print 'Count: ', count
    print 'Sum: ', sum
