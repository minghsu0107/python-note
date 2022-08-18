class Bank_acount:
    def __init__(self):
        self._password = '0000'

    @property
    def password(self):
        print("getter")
        return self._password

    @password.setter
    def password(self, value):
        print("setter")
        self._password = value

    @password.deleter
    def password(self):
        del self._password
        print('del complete')

if __name__ == '__main__':
  andy = Bank_acount()
  # getter
  print(andy.password)

  # setter
  andy.password = '1234'
  print(andy.password)

  del andy.password
