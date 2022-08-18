# __getitem__()與__setitem__()則用來設定[]運算子的行為
class Some:
    def __init__(self):
        self.inner = {}

    def __setitem__(self, name, value):
        self.inner[name] = value

    def __getitem__(self, name):
        return self.inner[name]


s = Some()
s[0] = 100
s['Justin'] = 'Message'
print(s[0])
print(s['Justin'])
