def calc(o, h):
    new = o + (o * (h / 100))
    return new

oldsalary = float(input("Enter the old salary: "))
hike = float(input("Enter the hike percentage: "))
newsalary = calc(oldsalary, hike)
print("New Salary :", newsalary)
