def increament(list2):
    for i in range(0,len(list2)):
        list2[i] += 5
    print(list2)

list1 = [10,20,30,40,50]
print(list1)
increament(list1)
print(list1)

def inc(listB):
    print("ID of the inside func before assign: ",id(listB))
    listB = [1,2,3,4,5]
    for i in range(0,len(listB)):
        listB[i] += 5
    print("Id of list changed inside func after assign: ",id(listB))
    print("The list inside the funcafter argument: ")
    print(listB)

print("Id of list changed inside func after assign: ",id(listA))
print("The list inside the funcafter argument: ")
print(listA)
inc(listA)
print(listA)    

