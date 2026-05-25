quan = list(map(float, input("Enter quantities of products (comma-separated): ").split(",")))
pri = list(map(float, input("Enter prices of products (comma-separated): ").split(",")))
total = 0
for i in range(len(quan)):
    total += quan[i] * pri[i]
print(f"Total value of the inventory: {total :.2f}")