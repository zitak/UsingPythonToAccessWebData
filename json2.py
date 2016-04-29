import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input('Enter location: ')
#address = "South Federal University"
if len(address) >= 1:

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
    else:
        place = js["results"][0]["place_id"]
        print 'Place in', place

