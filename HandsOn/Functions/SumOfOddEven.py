def sum():
    n = int(input("Enter the range: "))

    odd = 0
    even = 0
    for i in range(n):
        num = int(input("Enter the num: "))
        if num % 2 == 0:
            even += num
        else:
            odd += num

    print("Sum of Odd num : ",odd)
    print("Sum of even num : ",even)

sum()    

