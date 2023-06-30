# 1 Hello, World!: Write a Python program that prints "Hello, World!" to the console.
print("Hello, World!")

# 2 Data Type Play: Create variables of each data type (integer, float, string, boolean, list, 
# tuple, dictionary, set) and print their types and values.
# Integer
integer_variable = 10
# Float
float_variable = 3.14
# String
string_variable = "Hello, World!"
# Boolean
boolean_variable = True
# List
list_variable = [1, 2, 3, 4, 5]
# Tuple
tuple_variable = (6, 7, 8, 9, 10)
# Dictionary
dictionary_variable = {"name": "John", "age": 25, "city": "New York"}
# Set
set_variable = {1, 2, 3, 4, 5}

# Print type and value of each variable
print(f"Type of integer_variable: {type(integer_variable)}, value: {integer_variable}")
print(f"Type of float_variable: {type(float_variable)}, value: {float_variable}")
print(f"Type of string_variable: {type(string_variable)}, value: {string_variable}")
print(f"Type of boolean_variable: {type(boolean_variable)}, value: {boolean_variable}")
print(f"Type of list_variable: {type(list_variable)}, value: {list_variable}")
print(f"Type of tuple_variable: {type(tuple_variable)}, value: {tuple_variable}")
print(f"Type of dictionary_variable: {type(dictionary_variable)}, value: {dictionary_variable}")
print(f"Type of set_variable: {type(set_variable)}, value: {set_variable}")

# 3List Operations: Write a Python program to create a list of numbers from 1 to 10, 
# and then add a number, remove a number, and sort the list.
# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
# Print the initial list
print("Initial list:", numbers)
# Add a number
numbers.append(20)
# Remove a number
numbers.remove(3)
# Sort the list
numbers.sort()
# Print the updated list
print("Updated list:", numbers)

# 4Sum and Average: Write a Python program that calculates and prints the sum and 
# average of a list of numbers.
def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Input list of numbers
numbers = [10, 20, 30, 40]

# Calculate sum
sum_result = calculate_sum(numbers)

# Calculate average
average_result = calculate_average(numbers)

# Print the results
print("Sum:", sum_result)
print("Average:", average_result)


# 5 String Reversal: Write a Python function that takes a string 
# and returns the string in reverse order.
def reverse_string(input_string):
    return input_string[::-1]

# Input string
input_string = "Python"

# Call the function and print the result
reversed_string = reverse_string(input_string)
print(reversed_string)


# 6 **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Input string
input_string = "Hello"

# Call the function and print the result
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)

# 7Factorial Calculation: Write a Python function that calculates the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5

# Call the function and print the result
factorial_result = factorial(number)
print(f"Factorial of {number} is {factorial_result}.")

# 8. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in 
# the Fibonacci sequence.

def fibonacci(n):
    sequence = [0, 1]

    if n <= 2:
        return sequence[:n]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Input number
n = 5

# Call the function and print the result
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)


# 10. **List Comprehension**: Use list comprehension to create a list of the squares 
# of the numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]

print(squares)

