name = input('請輸入檔名：')
file = open(name, 'r', encoding='UTF-8')
content = file.read()
print(content)
file.close()

with open('hola.txt', 'r') as f:
    print(f.read(), end='')