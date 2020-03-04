## sorts are all stable
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))   # sort by age
from operator import itemgetter, attrgetter
print(sorted(student_tuples, key=itemgetter(2), reverse = True))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_objects, key=lambda student: student.age))   # sort by age
print(sorted(student_objects, key=attrgetter('age')))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

my_alphabet = ['a', 'b', 'c'] 
def custom_key(word): 
    numbers = [] 
    for letter in word: 
       numbers.append(my_alphabet.index(letter)) 
    return numbers 
# python中的整数列表能够比较大小 
# custom_key('cbaba')==[2, 1, 0, 1, 0] 
x = ['cbaba', 'ababa', 'bbaa'] 
x.sort(key=custom_key)
print(x)

def cmp_ignore_case(s1, s2):
    t1=s1.lower();
    t2=s2.lower();
    if(t1>t2):
        return 1
    if(t1==t2):
        return 0
    return -1
import functools
print(sorted(['bob', 'about', 'Zoo', 'Credit'], \
             key = functools.cmp_to_key(cmp_ignore_case)))

a = [[3, 4], [3, 2], [1, 2], [2, 5]]
print(sorted(a)) # [[1, 2], [2, 5], [3, 2], [3, 4]]
