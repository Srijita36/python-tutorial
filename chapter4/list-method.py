_variableOne = ["Apple", "Medicine", 22, 32.23, True, False, "srijita"]

print(_variableOne)


# 1. append()
# Syntax: list.append(item)

_variableOne.append("majumder") # Adds 'NewItems' at the end 

print(_variableOne) #Output ['Apple', 'Medicine', 22, 32.23, True, False, 'srijita', 'majumder']

# 2. insert()
# Syntax: list.insert(index, item)

_variableOne.insert(2,"Rahul") # Inserts at index 2

print(_variableOne) # Output ['Apple', 'Medicine', 'Rahul', 22, 32.23, True, False, 'srijita', 'majumder']


# 3. remove()
# Syntax: list.remove(item)

_variableOne.remove(32.23)  # Removes the item by value

print(_variableOne) # Output ['Apple', 'Medicine', 'Rahul', 22, True, False, 'srijita', 'majumder']



# 4. pop()
# Syntax: list.pop()


_variableOne.pop(3)

print(_variableOne)

pop_item=_variableOne.pop(3) # The Item popping our 

print(pop_item) # Output True

_variableOne.pop() # It will popping out the last element of the list 


print(f"Popping out the Last element{_variableOne}")


# 5. index()
# Syntax: list.index(item)
print("\n5. index(item) Method:")
_indexOfSrijita = _variableOne.index("Srijita")  # Gets index of 'Srijita'
print(f"Index of 'Srijita': {_indexOfSrijita}")
# Output: Index of 'Srijita': 6


# 6. count()
# Syntax: list.count(item)
print("\n6. count(item) Method:")
_variableOne.append(22)  # Adding another 22
print("List after appending 22:", _variableOne)
_count22 = _variableOne.count(22)  # Counts how many times 22 appears
print(f"Count of 22: {_count22}")
# Output: Count of 22: 2
_variableOne.pop()  # Remove the extra 22 added above



# 7. reverse()
# Syntax: list.reverse()
print("\n7. reverse() Method:")
_variableOne.reverse()  # Reverses the list in-place
print(f"After reverse: {_variableOne}")
# Output: ['Srijita', False, True, 32.23, 22, 'Medicine', 'Apple']



# 8. sort()
# Syntax: list.sort()
print("\n8. sort() Method:")
numeric_list = [5, 2, 9, 1]
print("Original numeric list:", numeric_list)
numeric_list.sort()  # Sorts in ascending order
print(f"Sorted list: {numeric_list}")
# Output: [1, 2, 5, 9]

# Also demonstrating reverse sort
numeric_list.reverse()
print(f"After reverse sort: {numeric_list}")
# Output: [9, 5, 2, 1]



# 9. copy()
# Syntax: list.copy()
print("\n9. copy() Method:")
copied_list = _variableOne.copy()  # Creates a shallow copy
print("Copied list:", copied_list)
# Output: Same as current _variableOne



# 10. clear()
# Syntax: list.clear()
print("\n10. clear() Method:")
temp_list = _variableOne.copy()  # Copy before clearing
temp_list.clear()  # Removes all elements
print("After clear:", temp_list)
# Output: []