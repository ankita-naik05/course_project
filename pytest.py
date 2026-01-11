import sys

def product_details(product_id, product_name, price, quantity):
    total_cost = price * quantity
    discount = "Eligible" if total_cost >= 5000 else "Not Eligible"

    return {
        "Product ID": product_id,
        "Product Name": product_name,
        "Price": price,
        "Quantity": quantity,
        "Total Cost": total_cost,
        "Discount": discount
    }

if __name__ == "__main__":
    product_id = sys.argv[1]
    product_name = sys.argv[2]
    price = float(sys.argv[3])
    quantity = int(sys.argv[4])

    result = product_details(product_id, product_name, price, quantity)

    print("\n--- Product Details ---")
    for key, value in result.items():
        print(f"{key:15}: {value}")
