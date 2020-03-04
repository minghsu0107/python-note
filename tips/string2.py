ch1 = 'a'
ch2 = '7'

print(ch1 in '0123456789') #False

print(ch2 in '0123456789') #True

import string
input_str = input()
lower, upper, digit = 0, 0, 0
for c in input_str:
    if c in string.ascii_lowercase:
        lower += 1
    elif c in string.ascii_uppercase:
        upper += 1
    elif c in string.digits:
        digit += 1
print(lower, upper, digit)