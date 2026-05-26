def prime(x, y):
    if x > y:
        print("Provide valid input")
        return
    for i in range(x, y + 1):
        if i > 1: 
            count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1
            if count == 2:
                print(i, end=" ")
x = int(input("Enter start number: "))
y = int(input("Enter end number: "))
prime(x, y)            