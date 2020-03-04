name = input('請輸入檔名：')
file = open(name, 'w', encoding = 'UTF-8') # if file does not exit, create it
file.write('test')
file.close()

with open(name, 'w') as f:
	print("hello", file = f)