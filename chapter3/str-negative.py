# Assign the string "Harsh" to the variable _name
_name = "Harsh"

# Print the string from index 0 to the end
print(_name[0 : ])  # Output: Harsh

# Print the characters from index -4 to -1 (excluding -1)
# -4 = 'a', -3 = 'r', -2 = 's' => so the result is 'ars'
print(_name[-4 : -1])  # Output: ars

# Print characters from index 1 to 3 (index 4 is excluded)
# index 1 = 'a', index 2 = 'r', index 3 = 's'
print(_name[1 : 4])  # Output: ars



R="Amazon"

r=R[-5:]

print(r)

S="Srijita"

m=S[-7:-1]

print(m)

p=S[:-3]

print(p)

b=S[-2:-4]

print(b)
