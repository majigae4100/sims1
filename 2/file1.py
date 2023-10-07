import requests


print(type(requests))
attrs = dir(requests)
for i in attrs:
    print(i)
    
print(requests.__name__)

print(hasattr(requests.__name__,))


'''     
class Human():
    pass


class Student(Human):
    pass


print(issubclass(Student, Human))
'''

