myObj = open("myfile.txt", "r")
var = myObj.read(10) # for passing argument for certain char read
print(var)
myObj.close()

myObj = open("myfile.txt", "r")
var = myObj.read() # for no or neg num passing argument for read entire line
print(var)
myObj.close()

myObj = open("myfile.txt", "r")
var = myObj.readlines(10) # similar to read
print(var)
myObj.close()

#readlines method
myObj = open("myfile.txt", "r")
d = myObj.readlines()
for line in d:
    words=line.split()
    print(words)

myObj = open("myfile.txt", "r")
d = myObj.readlines()
for line in d:
    words=line.splitlines()
    print(words)    

myObj = open("myfile.txt", "r")
d = myObj.readlines()
for line in d:
    words=line
    print(words)     