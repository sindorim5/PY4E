import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	url = input('Enter location: ')
	if len(url) < 1: break

	print('Retrieving', url)
	uh = urllib.request.urlopen(url, context=ctx)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None
		print('==== Failure To Retrieve ====')
		continue

	comments = js["comments"]
	sum = 0
	for comment in comments:
		sum += int(comment['count'])

	print('Count:', len(comments))
	print('Sum:', sum)
