def letter(n):
   if n>=0 and n<=9:
        #for i in range(n):
           number = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
           print(number[n])
   else:
        print("Invalid input")     
num = int(input("Enter the number: "))
letter(num)