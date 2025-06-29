# Define the tuple
_newTuple = (1, 2, "Srijita", 22.22, True, False)

# 1. count(value): Returns the number of times a value appears in the tuple
print("\n1. count(value) Method:")
count_true = _newTuple.count(True)
print(f"Count of True in {_newTuple} is: {count_true}")  # Output: 1

count_2 = _newTuple.count(2)
print(f"Count of 2 in {_newTuple} is: {count_2}")  # Output: 1



# 2. index(value): Returns the index of the first occurrence of the value
print("\n2. index(value) Method:")
index_Srijita = _newTuple.index("Srijita")
print(f"Index of 'Srijita' in {_newTuple} is: {index_Srijita}")  # Output: 2

index_22_22 = _newTuple.index(22.22)
print(f"Index of 22.22 in {_newTuple} is: {index_22_22}")  # Output: 3




# 3. len(): Not a method, but a built-in function to get length
print("\n3. len() Function:")
print(f"Length of {_newTuple} is: {len(_newTuple)}")  # Output: 6



# 4. Using 'in' keyword to check existence
print("\n4. Membership Test with 'in':")
print(f"Is 'Srijita' in {_newTuple}? {'Srijita' in _newTuple}")  # Output: True
print(f"Is 5 in {_newTuple}? {5 in _newTuple}")  # Output: False