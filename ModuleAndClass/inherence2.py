class Account:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError('餘額不足')

    def __str__(self):
        return ('Id:\t\t' + self.id +
                '\nName:\t\t' + self.name +
                '\nBalance:\t' + str(self.balance))

class CheckingAccount(Account):
    def __init__(self, id, name):
        super(CheckingAccount, self).__init__(id, name) #呼叫CheckingAccount的父類別的__init__()
        self.overdraftlimit = 30000

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraftlimit:
            self.balance -= amount
        else:
            raise ValueError('超出信用')

    def __str__(self):
        return (super(CheckingAccount, self).__str__() + 
                '\nOverdraft limit\t' + str(self.overdraftlimit));

acct = CheckingAccount('E1234', 'Justin Lin')
print(acct, end = '\n\n')
acct.deposit(1000)      # 使用 Account 的 deposit() 定義
print(acct, end='\n\n')
acct.withdraw(2000)     # 使用 CheckingAccount 的 withdraw() 定義
print(acct, end='\n\n')