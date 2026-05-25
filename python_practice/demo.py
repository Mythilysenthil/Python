# Example: Number datatype
num1 = 10
print(type(num1))
# Example of float datatype
num2 = 4.0
print(type(num2))
# Example of boolean datatype
var1 = True
print(type(var1))
# Example of string datatype 
str1 = "Hello, World!"
print(str1)
# Example of list
list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1[2]))
#To create tuple
tuple1=(10,20,"Apple",3.4)
print(type(tuple1[1]))
#create a set
set1={10,20,"Mythily"}
print(set1)
print(type(set1))
#Example of none
myVar=None
print(type(myVar))
#Example:ceate a dictionary
student={"name":"Mythily","age":"21"}
print(student)
print(type(student))
print(student["age"])

# Literals : Boolean
x = (1==True) 
print(x)
Y = (1==False)
print(Y)
a = True+4
print(a)
b = False+10
print(b)

# Explample of identity operator
num_1=5;
print(type(num1) is int)
num_2=num_1
id(num1)
id(num2)
print(num1 is not num2 )

# membership operator
a = [1,2,3]
2 in a
'1' in a

# Example of explicit type conversion
num1 = 10
num2 = 20
num3 = num1 + num2
print(num3)
print(type(num3))
num4 = float(num1 + num2)
print(num4)
print(type(num4))

# input function
name = input("Enter your name: ")
age = (input("Enter your age: "))
print(type(age))

# printing a string
print("Hello, World!")
# printing multiple values
x = 5
y = 10
print("The value of x is", x, "and the value of y is", y)
#Formatting with f-strings
name = "Mythily"
age = 21
print(f"My name is {name} and I am {age} years old.")
# print
print('apple', 'banana', 'cherry', sep=',' , end='.\n') #here , and .printed but using the separator and end is used to print the next line after the output