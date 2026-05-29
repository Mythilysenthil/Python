def safe_division(a,b):
    try:    
       c = a/b
       print(c)
    except(ZeroDivisionError):
       print("Error: Division by zero!")  
n1 = int(input("Enter a: "))
n2 = int(input("Enter b: "))
safe_division(n1 ,n2)   