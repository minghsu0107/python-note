name = input('請輸入檔名：')
for line in open(name, 'r', encoding='UTF-8'):
    print(line, end='')

### 更有效率的方式，是呼叫檔案物件的next()方法，next()方法每次傳回下一行，
### 並在沒有資料可讀取時丟出StopIteration。可以使用for迴圈自動呼叫next()方法，
### 並在捕捉到StopIteration時離開迴圈