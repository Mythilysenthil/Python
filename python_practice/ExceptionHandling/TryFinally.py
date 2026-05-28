try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(c)   
except Exception:
    print("Can't div by zero")
    print(Exception)
else:    
    print("I will execute when no exception occurs")
finally:
    print("I am always executed")               