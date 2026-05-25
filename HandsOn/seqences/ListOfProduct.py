list = input("Enter a list of product names separated by commas: ").split(",")
print("List of products:")
for product in list:
    print(product.strip())