income = float(input("Enter your monthly income: "))
exp = (input("Enter your expenses (space-separated): "))
spendSplit = exp.split()
spendings = 0
for i in spendSplit:
    spendings+=float(i)
savings = income - spendings
print("Remaining Budget : ",savings)