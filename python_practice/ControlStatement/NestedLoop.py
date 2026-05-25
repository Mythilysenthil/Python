L = int(input("Enter Lower limit: "))
U = int(input("Enter Upper limit: "))
print("The prime numbers between", L, "to", U)
for num in range(L, U + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)