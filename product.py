import pytest
def product_details(name, p_id, quantity, price):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {p_id}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result

if __name__ == "__main__":
   
        name = "Laptop\n"
        p_id = "201\n"
        quantity = "4\n"
        price = 55000
        print(product_details(name, p_id, quantity, price))