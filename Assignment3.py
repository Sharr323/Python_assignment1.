# Question 1

def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

while True:
    try:
        user_input = int(input("Enter an integer: "))
        result = classify_number(user_input)
        print("Classification:", result)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


 #Question 2

def calculate_average(*args):
    """
    Calculates the average of any number of numeric arguments.

    Parameters:
    *args: A variable number of numeric values.

    Returns:
    float: The average of the input numbers.
    """
    if not args:
        return 0
    return sum(args) / len(args)

# Example
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
print("Average:", calculate_average(*numbers))

#Question 3

while True:
    try:
        number = float(input("Enter a number: "))
        print("You entered:", number)
        break
    except ValueError:
        print("Oops! That's not a valid number. Try again.")

#Question 4

names = input("Enter names separated by commas: ").split(',')

# Write to file
with open("names.txt", "w") as file:
    for name in names:
        file.write(name.strip() + "\n")

# Read from file
print("\nNames in file:")
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())


#Question 5

celsius_list = [float(temp) for temp in input("Enter Celsius temperatures separated by spaces: ").split()]
fahrenheit_list = list(map(lambda c: c * 9/5 + 32, celsius_list))

print("Fahrenheit temperatures:", fahrenheit_list)


#Question 6

def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input types. Please enter numbers.")

# Example
try:
    num = float(input("Enter numerator: "))
    denom = float(input("Enter denominator: "))
    output = divide_numbers(num, denom)
    if output is not None:
        print("Result:", output)
except ValueError:
    print("Error: Please enter valid numeric values.")


#Question 7

# Define the custom exception
class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""
    pass

# Function that checks if a number is positive
def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative number detected!")
    else:
        print("Number is positive or zero.")

# Demonstration with user input
while True:
    try:
        num = int(input("Enter a number: "))
        check_positive(num)
        break  # Exit loop if no exception
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except NegativeNumberError as e:
        print("Error:", e)


#Question 8

import random

def generate_random_numbers(count=10):
    return [random.randint(1, 100) for _ in range(count)]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Generate and display
numbers = generate_random_numbers()
print("Generated numbers:", numbers)
print("Average:", calculate_average(numbers))


#Question 9

import re

# I. Extract email addresses
text = input("Enter text with emails: ")
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print("Extracted emails:", emails)

# II. Validate date format YYYY-MM-DD
date = input("Enter a date (YYYY-MM-DD): ")
if re.fullmatch(r'\d{4}-\d{2}-\d{2}', date):
    print("Valid date format.")
else:
    print("Invalid date format.")

# III. Replace word
original_text = input("Enter a sentence: ")
word_to_replace = input("Word to replace: ")
replacement = input("Replacement word: ")
new_text = re.sub(rf'\b{word_to_replace}\b', replacement, original_text)
print("Updated sentence:", new_text)

# IV. Split by non-alphanumeric characters
split_text = input("Enter a string to split: ")
parts = re.split(r'\W+', split_text)
print("Split parts:", parts)


#Question 10

import socket

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 12345))
        server.listen(1)
        print("Server listening on port 12345...")
        conn, addr = server.accept()
        print("Connected by", addr)
        conn.sendall(b"Hello from server!")
        conn.close()
    except Exception as e:
        print("Server error:", e)

start_server()

#Client.py

import socket

def connect_to_server():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 12345))
        message = client.recv(1024)
        print("Received:", message.decode())
        client.close()
    except Exception as e:
        print("Client error:", e)

connect_to_server()


#Question 11
#making a GET request with requests
import requests

response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed with status code:", response.status_code)

#Connecting to SQLite in python

import sqlite3

# Step 1: Connect to database (or create it)
conn = sqlite3.connect("example.db")

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Step 4: Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

# Step 5: Commit changes
conn.commit()

# Step 6: Query data
cursor.execute("SELECT * FROM users")
print("Users:", cursor.fetchall())

# Step 7: Close connection
conn.close()













