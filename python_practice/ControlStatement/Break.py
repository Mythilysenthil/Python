N = int(input("Enter the value of N: "))
i = 1
sum = 0
while i <= N:
    num = int(input("Enter a number: "))    
    if num == 1:
        break
    else:
      sum += num
    i += 1
print("Sum =", sum)