squ = {} # without comprension
for x in range(5):
    squ[x]= x*x
print(squ)


squ = {x : x*x for x in range(5)} # with comprension
print(squ)