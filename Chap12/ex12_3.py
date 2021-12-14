import urllib.request, urllib.parse, urllib.error

url = input("Enter URL - ")
try:
	fhand = urllib.request.urlopen(url)
except:
	print("Invalid Web Address!")
	quit()
data = fhand.read().decode()
print(data[:3000])
print("Characters:", len(data))
