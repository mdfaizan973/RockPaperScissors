# Problem 1: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Problem 2: Display numbers from a list using loop / numbers = [12, 75, 150, 180, 145, 525, 50]
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break 
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

# Problem 3: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

middle_index = len(s1) 
s3 = s1[:middle_index] + s2 + s1[middle_index:]

print(s3)

# Problem 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"

lowercase_chars = []
uppercase_chars = []

for char in str1:
    if char.islower():
        lowercase_chars.append(char)
    else:
        uppercase_chars.append(char)

arranged_str = ''.join(lowercase_chars + uppercase_chars)

print(arranged_str)

# Problem 5: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []

for i in range(min(len(list1), len(list2))):
    new_list.append(list1[i] + list2[i])

# Add any leftover items from list1
new_list.extend(list1[len(list2):])

# Add any leftover items from list2
new_list.extend(list2[len(list1):])

print(new_list)

# Problem 6: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

new_list = [a + b for a, b in zip(list1, list2)]

# Add any leftover items from list1
new_list.extend(list1[len(list2):])

# Add any leftover items from list2
new_list.extend(list2[len(list1):])

print(new_list)

#Problem 7: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)
    
# Problem 8: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = {employee: defaults for employee in employees}

print(result)

# Problem 9: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)

# Problem 10: Modify the tuple
tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list
list1 = list(tuple1)

# Modify the first item of the list
list1[1][0] = 222

# Convert the list back to a tuple
tuple1 = tuple(list1)

print(tuple1)
