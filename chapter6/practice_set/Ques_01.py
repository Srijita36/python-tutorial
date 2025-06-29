# Write a program to find the greatest of four numbers entered by the user. 

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))
d = int(input("Enter 4th Number: "))

g = a

if b > g:
    g = b
if c > g:
    g = c
if d > g:
    g = d

print("The g number is:", g)
