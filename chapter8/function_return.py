# Example 1

def goodday(name , ending):
    print("Have a Good Day\t" + name)
    print(ending)
    return "Okay"


test=goodday("Srijita", "Bye Bye")

print(test)


#example 2


# Function Definition

def avg():
    a=int(input("Enter a Number:"))
    b=int(input("Enter a Number:"))
    c=int(input("Enter a Number:"))

    average=(a+b+c)/3
    print(average)

    return average



a=avg()    #Function Call

print(a)