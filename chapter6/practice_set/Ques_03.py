# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.


a ="Make a lot of money"
b ="buy now"
c ="subscribe this"
d ="click this"


test =input("Enter you comment:").strip().lower()

if a.lower() in test or b.lower() in test or c.lower() in test or d.lower() in test :

    print("This is a spam message")

else:
    print(" This is a normal message")    