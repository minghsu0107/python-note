import sys

if __name__ == '__main__':
    print(sys.argv)
# 該程式可能有「單獨執行」
# （例如執行一些本身的單元測試）與「被引用」兩種情況，因此用上述判斷就可以將這兩種情況區分出來


# $ python hello.py
# ['hello.py']

# $ python hello.py abc 123
### ['hello.py', 'abc', '123']

# 亦即 sys 模組的 argv 會紀錄執行程式時使用者給予的字串參數（包括所執行的程式名稱)，
# 程式可以根據這資訊做適當處理
