import traceback
x = 0
try:
    print(5 / x)
except:
    print("Something wrong")

arr = []
try:
    print(arr[0])
except:
    print("could not print ")
else:
    print("success")
finally:  # always do after try
    print("right or wrong")


def parse_int(s):
    try:
        print("parsing", s)
        x = int(s)
        print("result is", x)
    except ValueError:
        print("Invalid input", s)


def div_str(s, t):
    a = int(s)
    b = int(t)
    return a / b


def main():
    try:
        s = input()
        t = input()
        r = div_str(s, t)
        print(r)
    except ValueError:
        print("Invalid value")
    except ZeroDivisionError:
        print("div by 0")
    except:
        print("Something wrong")


while True:
    try:
        input = int(input('輸入整數：'))
        print('{0} 為 {1}'.format(input, '奇數' if input % 2 else '偶數'))
        break
    except ValueError:
        print('請輸入阿拉伯數字')
    except (EOFError, KeyboardInterrupt):
        print('使用者中斷程式')
    except:
        print('不明的程式中斷')
        traceback.print_exc()

file = open("greet.py", "r", encoding="UTF-8")
try:
    for word in file:
        print(word, end='')
except:
    print("error while reading file")
finally:
    file.close()
