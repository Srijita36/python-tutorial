# 3 WAYS TO WRITE A STRING

A='srijita'
B="srijita"
C='''srijita'''


# slicing of a string

Q= "Rahul"

b=Q[:4] # [start_index:end_index]

# start index is included but last index is not be included








# Step jump in string

A="pneumonoultramicroscopicsilicovolcanoconiosis"

T=A[1:9:2]

print (T)# Output -> nuoo



# Assign an integer
_no = 1234567890

# Convert the number to a string for slicing
_no_str = str(_no)

# Print characters from index 1 to 6 with step 2: indices 1, 3, 5
print(_no_str[1 : 7 : 2])  # Output: 35  (indexes 1='2', 3='4', 5='6')

# Print every 3rd character starting from index 0
print(_no_str[0 : : 3])    # Output: 1470 (indexes 0,3,6,9)

