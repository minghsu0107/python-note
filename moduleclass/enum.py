from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

print(Color.RED) # Color.RED
print(Color.RED.value) # red
my_color = 'red'
print(Color(my_color).value) # red
