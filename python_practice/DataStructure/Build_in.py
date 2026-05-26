str = "Good Day"
str1 = 'sadsaf12412'
print(str.upper()) #To make uppercase
print(str.lower()) #To make Lowercase
print(str.find('a')) #To find char and return integer
print(str.find('Da')) #To find certain char and return integer
print(str.count('o'))
print(str.capitalize())
print(str1.isalnum())
print(str1.isalpha())
print(str.endswith("to learn"))
print(str.startswith("Hello!"))

#palindrome
if str==str[::-1]:
    print("Given is palindrome")
else:
    print("Given is not a palindrome")    

# instead of using ==
print(str.__eq__(str[::-1]))  

#count the occurances
total_digit = 0
total_alpha = 0
for s in str:
    if s.isnumeric():
        total_digit += 1
    elif s.isalpha():
        total_alpha += 1
    else:
        pass
print("Count of letter: ",total_alpha)
print("Count of digit: ",total_digit)        


