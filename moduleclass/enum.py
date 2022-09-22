from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Color.RED
print(Color.RED)
# 1
print(Color.RED.value)
