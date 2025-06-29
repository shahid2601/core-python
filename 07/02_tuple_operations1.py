# Tuple does not support item appending or item deletion

# Create a tuple
my_tuple = ("admin1", "admin2", "admin3", "admin4")

# 1. Packing a tuple
my_tuple_packed = ("admin1", "admin2", "admin3", "admin4")
print("Packed Tuple: " + str(my_tuple_packed))  # The tuple is represented as a string

# 2. Unpacking a tuple
dept1, dept2, dept3, dept4 = my_tuple_packed  # Unpacking the my_tuple_packed into separate variables

print("Unpacked Tuple:")
print(dept1)
print(dept2)
print(dept3)
print(dept4)

# 3. Checking if an item is present in the tuple
print("Is 'admin1' in my_tuple_packed? " + str("admin7" in my_tuple_packed)) # Output: False

# 4. Multiple assignment using tuple unpacking

def get_coordinates():
    return (10, 20)

x, y = get_coordinates() # Unpacking the retuned tuple into x and y
print(x, y)