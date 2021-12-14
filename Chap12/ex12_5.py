import socket

url = input("Enter URL - ")
try:
	host = url.split("/")[2]
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((host, 80))
	cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
	mysock.send(cmd.encode())
except:
	print("Invalid Web Address!")
	quit()
received_data = b""
while True:
	data = mysock.recv(512)
	if (len(data) < 1):
		break
	received_data += data
received_data = received_data.decode()
start = received_data.find('\r\n\r\n') + 4
print(received_data[start:], end = "")
mysock.close()
