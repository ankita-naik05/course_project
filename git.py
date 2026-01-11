# Program to display product details

# Input from user
product_id = input("Enter Product ID: ")
product_name = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))

# Calculate total cost
total_cost = price * quantity

# Display product details
print("\n--- Product Details ---")
print("Product ID     :", product_id)
print("Product Name   :", product_name)
print("Price          :", price)
print("Quantity       :", quantity)
print("Total Cost     :", total_cost)

# Check discount eligibility
if total_cost >= 5000:
    print("Discount       : Eligible")
else:
    print("Discount       : Not Eligible")
