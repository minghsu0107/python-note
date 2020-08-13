with open('test.txt', 'r', encoding='UTF-8') as file:
    s = file.read(7)
    print(s)
    s = file.read(7)
    print(s)

    file.seek(0)

    s = file.read(7)
    print(s)
    s = file.read(7)
    print(s)
