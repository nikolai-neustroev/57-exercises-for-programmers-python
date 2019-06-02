# 10.
# Self-Checkout

print("Enter the price of item 1:")
price_item_1 = float(input())
print("Enter the quantity of item 1:")
quantity_item_1 = float(input())
print("Enter the price of item 2:")
price_item_2 = float(input())
print("Enter the quantity of item 2:")
quantity_item_2 = float(input())
print("Enter the price of item 3:")
price_item_3 = float(input())
print("Enter the quantity of item 3:")
quantity_item_3 = float(input())

subtotal = round(price_item_1 * quantity_item_1 + quantity_item_2 * price_item_2 + quantity_item_3 * price_item_3, 2)
tax = round(subtotal * 0.055, 2)
total = round(subtotal + tax, 2)

print(f"""Subtotal: ${subtotal}
Tax: ${tax}
Total: ${total}""")
