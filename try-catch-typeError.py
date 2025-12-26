print("start:")
print("exception handling with specific error type:")
try:
    print(15/"ten")
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print("we can't divide the value with zero")
print("stop")
OUTPUT:
start:
exception handling with specific error type:
Unsupported operation
stop
