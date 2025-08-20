  # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Constant (written in uppercase)
TAX_RATE = 0.20  # 20% tax

# Variables
customer_name = "Ruvarashe Magaya"
item = "Wooden Dining Table"
price = 350.00  # in USD
quantity = 2

# Calculations
subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

# Output using print function
print("Customer Name:", customer_name)
print("Item Purchased:", item)
print("Quantity:", quantity)
print("Price per Item: $", price)
print("Subtotal: $", subtotal)
print("Tax (15%): $", tax)
print("Total Amount Due: $", total)
