"""
result = None
try:
    a = input("Enter digit: ")
    b = input("Enter digit: ")
    result = a / b
except TypeError:
    try:
        try:
            a = float(a)
            b = float(b)
            result = a / b
        except:
            if a.isdigit() and b.isdigit():
                result = int(a) / int(b)
    except Exception as ex:
        print(ex)

if result is not None:
    print(result)
"""

"""
result = None
try:
    a=input("Enter digit: ")
    b=input("Enter digit: ")
    result = a/b
except TypeError:
    try:
        a=float(a)
        b=float(b)
        result = a/b
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError {zde}")
    except Exception as ex:
        print(f"Exception: {ex}")
except ZeroDivisionError as zde:
    print(zde)
if(result != None):
    print(f"Result - {result}")
"""
from validation import Validator
from builderror import BuildError

limit = 10
amount = input("Enter amount: ")

try:
    amount = int(amount)
    check = Validator()
    error = BuildError(amount, limit)
    check.Check(error)
except TypeError as te:
    print("Wrong amount was entered!!!")
except BuildError as be:
    print(be)
