def add_mul(num1, num2, num3):
    out =( num1 + num2) * num3
    return out
val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
result = add_mul(1 ,2 , 3)
result = add_mul(1.1, 2.2, 3.3)
print("The sum is: ", result)