students = {1: 'Dima', 2: 'Roma', 3: 'Igor'}
iterator = iter(students)

'''try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))  # StopIteration
except StopIteration:
    pass'''  # StopIteration
'''
while next(iterator):
     print(next(iterator))
'''  # With while ^
'''from counter import Counter

try:
    counter = Counter(100, 0)
    for i in counter:
        print(i)
except StopIteration:
    pass'''  # Counter
from generator import Generator
generator = Generator(0)
j = 0
for i in generator.raise_to_the_degrees_F(3, 10):
    print(f"{j} - {i}")
    j += 1

