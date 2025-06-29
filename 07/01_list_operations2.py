my_list = [1, 2, 3, 4, 5]

# 1. Slicing a list
print(my_list[1:4])  # Output: [2, 3, 4]

# 2. Concatenating two lists
another_list = [6, 7, 8]
print(my_list + another_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 3. Sorting a list
unsorted_list = [7, 2, 5, 1, 4]
print(sorted(unsorted_list))  # Output: [1, 2, 4, 5, 7]

# 4. Checking if an element exists in a list
print(3 in my_list) # Output: True
print(10 in my_list) # Output: False