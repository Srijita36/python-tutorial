#Default Arguments

def goodday(name , ending="Thank You"):
    print("Have a Good Day\t" + name)
    print(ending)
 


goodday("Srijita", "Bye Bye") # If the user putting the 2nd value it will print user given value 
goodday("Harsh") # if user do not put any value then it will give the default value which is "Thank You"