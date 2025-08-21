 
# Constant (written in uppercase)
TAX_RATE = 0.20  # 20% tax

# Variables (written in lowercase)
customer_name = "Ruvarashe Magaya"
item = "Wooden Dining Table"
price = 350.00  # in USD
quantity = 2

# Calculations
subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

# Print function
print("Customer Name:", customer_name)
print("Item Purchased:", item)
print("Quantity:", quantity)
print("Price per Item: $", price)
print("Subtotal: $", subtotal)
print("Tax (15%): $", tax)
print("Total Amount Due: $", total)

