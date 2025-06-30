numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue # Skip the rest of the loop when number is 3
    print(number)  # This will not print 3
                    # Output: 1, 2, 4, 5