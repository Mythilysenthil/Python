#Fun definition
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
num = int(input("Enter a number: "))
res = factorial(num)
print("The factorial of ", num, " is: ", res)