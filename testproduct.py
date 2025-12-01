from product import product_details

def test_product_details():
    expected_output =(
        "Product Name: Laptop\n"
        "Product ID: E201\n"
        "Quantity: 40\n"
        "Price: 55000"
    )
    assert product_details("Laptop", "E201", 40, 55000) == expected_output