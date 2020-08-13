name = input('請輸入檔名：')
file = open(name, 'r', encoding='UTF-8')
for line in file.readlines():
    print(line, end='')
file.close()

name = input('請輸入檔名：')
with open(name, 'r', encoding='UTF-8') as file:
    for line in file:
        print(line, end='')

name = input('請輸入檔名：')
with open(name, 'r', encoding='UTF-8') as file:  # file.close after "with block"
    while True:
        line = file.readline()
        if line == '':
            break
        print(line, end="")
