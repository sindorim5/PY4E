import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Counts라는 테이블이 존재한다면 삭제
cur.execute('DROP TABLE IF EXISTS Counts')

# Counts라는 테이블을 만들고 TEXT형의 email행, INT형의 count행 생성
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): continue
	pieces = line.split()
	email = pieces[1]
	# ?는 placeholder 뒤의 email은 원소가 하나인 튜플
	cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
	# 첫번째 레코드를 읽어옴, GET과 비슷하다
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (email, count)
				VALUES (?, 1)''', (email,))
	else:
		cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
					(email,))
	# 데이터 갱신
	conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])

cur.close()
