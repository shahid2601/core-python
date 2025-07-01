# Create a set
my_set = {1, 2, 3, 4, 5}

# 1. Add an element to the set
my_set.add(6)
# print("After adding 6:", my_set)

# 2. Remove an element from the set
my_set.remove(3)
# print("After removing 3:", my_set)

# 3. Set Operations(Union, Intersection, Difference)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)
# print(union_set) # Will print {1, 2, 3, 4, 5, 6} because it combines all unique elements from both sets

# Intersection
intersection_set = set1.intersection(set2)
# print(intersection_set) # Will print {3, 4} because these are the common elements in both sets

# Difference
difference_set = set1.difference(set2)
# print(difference_set) # Will print {1, 2} because these are the elements in set1 that are not in set2

# 4. Subset and Superset
is_subset = set1.issubset(set2)
print(is_subset) # Output will be False because set1 is not a subset of set2
is_superset = set1.issuperset(set2)
print(is_superset) # Output will be False because set1 is not a superset of set2