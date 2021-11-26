import socket

# 소켓 만들고 가져오기, 아직 연결이 되지 않음
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # 주소의 80번 포트에 연결, 주소가 유효하지 않으면 에러남.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # cmd는 byte
mysock.send(cmd)

while True:
	data = mysock.recv(512) # 문자 512개를 받는다.
	if (len(data) < 1): # 문자를 0개 받으면 스트림이 끝났다는 뜻.
		break
	print(data.decode(), end='')
mysock.close() # 스트림을 닫는다.
