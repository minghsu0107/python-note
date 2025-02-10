from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)
    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

# we can initiate an instance flexibly with classmethod
person1 = Person.from_birth_year('John',1985)
person1.display()
