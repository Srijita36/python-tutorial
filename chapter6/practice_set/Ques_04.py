# Write a program to find whether a given username contains less than 10 
# characters or not.

give_user=str(input("Enter the Username:"))

length=len(give_user)

if (length>10):
    print("Yes, its greater than 10 ")

else:
    print("No, it is less than 10")    