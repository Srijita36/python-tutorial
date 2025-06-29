age = int(input("Enter Your Age, I'll tell you if the movie \"Fifty Shades of Grey\" is suitable for you or not: "))

# if else elif ladder

# indent

if (age > 18):
    print("This movie is 18+. You are allowed to watch it.")

elif(age<0):
    print("Negative Age Can not be valid")

elif(age==0):

    print("This Is Not a valid age")    


else:
    print("This is not for you. You're still a kid.")
