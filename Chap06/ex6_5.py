str = 'X-DSPAM-Confidence:	0.8475'
start = str.find(':')
data = str[start+1 : ]
data = data.strip()
number = float(data)
print(number)
