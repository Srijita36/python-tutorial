def factorial(n):
    if n==1 or n==0: # base condition which doesn’t call the function
        return 1
    return n*factorial(n-1)  # function calling itself 


n = int(input("Enter a number:"))
print(f"The factorial is {factorial(n)}")



