myObj = open("myfile.txt", "w")
count = myObj.write("Hello\nfrom\nmythily")
print(count)
myObj.close()

print("Now reading the content of the file")

myObj = open("myfile.txt", "r")
for str in myObj: 
    print(str)
myObj.close()