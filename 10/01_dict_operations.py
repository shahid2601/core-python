# Create a dictionary
student = {
    "name": "John",
    "age": 20,
    "stu_id": 12345,
    "branch": "Computer Science"
}

# 1. Access value by key
# print("Name:", student["name"]) # Output: Name: John

# 2. Modify value by key
# student["age"] = 18
# print("Updated Age:", student["age"]) # Output: Updated Age: 18

# 3. Add a new key-value pair
# student["is_passed"] = True
# print("Is Passed (new field added):", student["is_passed"]) # Output: Is Passed (new field added): True

# 4. Delete a key-value pair
# del student["branch"]
# print("After deleting branch:", student) # Output: After deleting branch: {'name': 'John', 'age': 18, 'stu_id': 12345, 'is_passed': True}

# 5. Check if a key exists
# if "stu_id" in student:
    # print("Student ID exists:", student["stu_id"]) # Output: Student ID exists: 12345

# 6. Iterate over keys and values
for key, value in student.items():
    print(f"{key}: {value}") # Will go through each key-value pair and print it