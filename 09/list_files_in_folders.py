import os # this module provides a way to interact with the operating system

paths = input("Enter the required list folder paths in space-separated format: ").split()  # Take input from the user as a multiple paths separated by space and split them into a list


for path in paths:  # Iterate through each path in the list
    try:  # exception handling to catch known errors like FileNotFoundError
        # Check if the path is a directory and list files in it
        files = os.listdir(path)
    except FileNotFoundError:  # If the directory does not exist, it will raise a FileNotFoundError
        print(f"The provided path '{path}' is not valid or does not exist. Please check the path and try again. ")
        continue  # Skip to the next iteration if the path is invalid

    print("=== Listing files in folder: " + path + " ===")  # Print the folder being processed

    for file in files:  # Iterate through each file in the directory
        print(file)  # Print the name of the file