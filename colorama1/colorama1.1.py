import colorama

print(type(colorama))
attrs = dir(colorama)
for i in attrs:
    print(i)

print(colorama.__name__)

print(hasattr(colorama.__name__,))