import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	url = input('Enter location: ')
	if len(url) < 1: break

	print('Retrieving', url)
	uh = urllib.request.urlopen(url, context=ctx)
	data = uh.read()
	print('Retrieved', len(data), 'characters')
	#print(data.decode())

	tree = ET.fromstring(data)

	counts = tree.findall('.//count')
	print('Count:', len(counts))
	sum = 0
	for count in counts:
		sum += int(count.text)
	print('Sum:', sum)
