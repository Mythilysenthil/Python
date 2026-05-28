try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(c)
except(ZeroDivisionError):
    print("Can't div by zero")
print("Run successfully")        