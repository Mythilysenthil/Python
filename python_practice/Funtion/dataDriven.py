def cir(radius):
    print(3.14 * radius * radius)
def rec(length, breadth):
    print(length * breadth)
def squ(side):
    print(side * side)

while True:
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        r = float(input("Enter the radius of the circle: "))
        cir(r)
    elif choice == 2:
        l = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the breadth of the rectangle: "))
        rec(l, b)
    elif choice == 3:
        s = float(input("Enter the side of the square: "))
        squ(s)
    elif choice == 4:
        break
    else:
        print("Invalid choice")