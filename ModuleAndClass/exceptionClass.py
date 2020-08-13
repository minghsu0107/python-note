class NotDigitError(Exception):
    pass


def is_digit(a):
    return ord(a) >= ord('0') and ord(a) <= ord('9')


def check_digit(a):
    if not is_digit(a):
        raise NotDigitError('error!')


check_digit("x")


class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')
