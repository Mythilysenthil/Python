mark = int(input("Enter your mark: "))
if mark > 90:
    print("Grade: O")
elif mark > 81 and mark <= 90:
    print("Grade: A")
elif mark > 71 and mark <= 80:
    print("Grade: B")  
elif mark > 60 and mark <= 70:     
    print("Grade: C")
elif mark >51 and mark <= 60:
    print("Grade: D")
else:
    print("Grade: F")