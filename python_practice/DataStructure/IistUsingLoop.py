listA = []
n = int(input("Enter the number of elements in list: "))
for i in range(0, n):
    print("Enter the element No-{}:".format(i + 1))
    elm = int(input())
    listA.append(elm)

print(listA)  