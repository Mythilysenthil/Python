list1 = [10, 20, 30, 40, 50]
while True:
    print("1. Append element")
    print("2. Insert element")
    print("3. Append a list to the given list")
    print("4. Pop element")
    print("5. Remove element")
    print("6. Sort ascending")
    print("7. Sort descending")
    print("8. Exit")

    n = int(input("Enter the choice: "))
    if n == 1:
        list1.append(60)
        print(list1)
    elif n == 2:
        list1.insert(1, 15)
        print(list1)
    elif n == 3:
        list2 = [60, 70, 80]
        list1.extend(list2)
        print(list1)
    elif n == 4:
        index = int(input("Enter the index position: ")) #1
        value = int(input("Enter new value: "))
        list1[index] = value #list1[1] = 5
        print(list1)    
    elif n == 5:
        list1.pop(2)
        print(list1)
    elif n == 6:
        list1.remove(40)
        print(list1)
    elif n == 7:
        list1.sort()
        print(list1)
    elif n == 8:
        list1.sort(reverse=True)
        print(list1)
    elif n == 9:
        break
    else:
        print("Invalid input")