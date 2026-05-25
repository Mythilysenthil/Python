def add_mul(num1, num2, num3):
    out =( num1 + num2) * num3
    return out

val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
val3 = int(input("Enter third number: "))
result = add_mul(val1, val2, val3)
print("The sum is: ", result)