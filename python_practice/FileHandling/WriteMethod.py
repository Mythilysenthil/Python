myObj = open("myfile.txt", "w")
count = myObj.write("Heyy i am mythily from salem\n")
print("No of characters written:", count)
myObj.close()


# writeline 
myObj = open("myfile.txt", "w")
lines = [
    "Hello everyone\n",
    "Writing multiline strings\n",
    "This is the third line"
]
myObj.writelines(lines)
myObj.close()        