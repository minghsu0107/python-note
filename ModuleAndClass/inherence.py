class Pet:
  def __init__(self, name):
    self.name = name # private
  def info(self):
    return "pet " + self.name
  def pat(self):
    print("I am " + self.info())

class Dog(Pet):
  def info(self):
    return "doggy " + self.name

class Cat(Pet):
  def __init__(self, name, color="white"):
    super().__init__(name)
    self._color = color
  def info(self):
    return self._color + " cat " + self.name

cat = Cat('KKK', 'blue')
cat.pat()
print(cat.info())

dog = Dog('DDD')
dog.pat()
print(dog.info())

### we can override superclass (base class)
### usinge super() to call superclass