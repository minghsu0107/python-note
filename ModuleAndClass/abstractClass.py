import random
from abc import ABCMeta, abstractmethod


class GuessGame(metaclass=ABCMeta):
    @abstractmethod
    def message(self, msg):
        pass

    @abstractmethod
    def guess(self):
        pass

    def go(self):
        self.message(self.welcome)
        number = int(random.random() * 10)
        while True:
            guess = self.guess()
            if guess > number:
                self.message(self.bigger)
            elif guess < number:
                self.message(self.smaller)
            else:
                break
        self.message(self.correct)


class ConsoleGame(GuessGame):
    def __init__(self):
        self.welcome = "歡迎"
        self.prompt = "輸入數字："
        self.correct = "猜中了"
        self.bigger = "你猜的比較大"
        self.smaller = "你猜的比較小"

    def message(self, msg):
        print(msg)

    def guess(self):
        return int(input(self.prompt))


game = ConsoleGame()
game.go()


class Flyer(metaclass=ABCMeta):  # 就像是Java中的interface
    @abstractmethod
    def fly(self):
        pass


class Bird:
    pass


class Sparrow(Bird, Flyer):  # 就像Java中繼承Bird類別並實作Flyer介面
    def fly(self):
        print('麻雀飛')


s = Sparrow()
s.fly()
