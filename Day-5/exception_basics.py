#prints all built-in exception modules
# print(dir(locals()['__builtins__']))

try:
    num1=int((input("Enter num1")))
    num2=int(input("Enter num 2"))
    print(num1/num2)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid value")
else:
    print("calculation successful")
finally:
    print("finally executed")

