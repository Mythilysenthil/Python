#only duplicates are mutable
my_set = {1,2,3,4,3,2}
print(my_set)

my_set = set([1,2,3,2])
print(my_set)

my_set = {1,2,(3,4)} #here only takes the tuple() not list[]
print(my_set)

my_set.add(2)
print(my_set)

# remove and discard func
my_set = {1,3,4,5,6}
print(my_set)
my_set.discard(4)
print(my_set)
my_set.remove(6)
print(my_set)
my_set.discard(2)
print(my_set)

# pop and clear
my_set = {1,3,4,5,6}
print(my_set)
print(my_set.pop())
my_set.clear()
print(my_set)