def increament(list2):
    for i in range(0, len(list2)):
        list2[i] += 5
    print(list2)


listA = [10, 20, 30, 40, 50]

print(listA)
increament(listA)
print(listA)


def inc(listB):
    print("ID of inside func before assign:", id(listB))

    listB = [1, 2, 3, 4, 5]   # new list created

    for i in range(0, len(listB)):
        listB[i] += 5

    print("ID of list changed inside func after assign:", id(listB))
    print("The list inside the func after argument:")
    print(listB)


print("ID of list before function call:", id(listA))
print("The list before function call:")
print(listA)

inc(listA)

print("List after function call:")
print(listA)