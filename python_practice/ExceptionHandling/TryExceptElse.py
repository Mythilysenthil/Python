try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(c)
except(ZeroDivisionError):
    print("Can't div by zero")
else:    
   print("I will execute when no exception occurs")


try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(c)
except NameError:
    print("This is value error")    
except Exception:
    print("Can't div by zero")
    print(Exception)
else:    
    print("I will execute when no exception occurs")           
