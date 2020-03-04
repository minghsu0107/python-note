class Some:
    class Iterator:
        def __init__(self, length):
            self.length = length
            self.number = -1
        def __next__(self):
            self.number = self.number + 1
            if self.number == self.length:
                raise StopIteration
            return self.number
    
    def __init__(self, length):
        self.length = length

    def __iter__(self):
        return Some.Iterator(self.length)


# 使用iter()來代為呼叫物件的__iter__()方法，
# 使用next()方法代為呼叫物件的__next__()方法。
# 事實上，你可以結合for in迴圈來提取物件，for in迴圈會透過__iter__()取得迭代器，
# 然後在每次迴圈中呼叫__next__()方法，而後遇到StopIteration丟出後離開迴圈

for i in Some(5):
    print(i)

s = Some(3)
it = iter(s)
print(next(it))   # 0
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # StopIteration