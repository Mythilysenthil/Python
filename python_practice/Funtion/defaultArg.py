def add_num(num1, num2, num3=4): # here num3 is a default argument
    out = (num1 + num2) * num3
    return out # Return a value from a function 
val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
result = add_num(val1, val2)
print("The sum is: ", result)