try:
    num=int(input("Enter a pos integer: "))
    if(num<=0):
        raise ValueError("This is an neg number") # which throw the error manually or generated
except ValueError as e: # which catch the error or handled the error
    print(e)
print("I am sucessfully handled")