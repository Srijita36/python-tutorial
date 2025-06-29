# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 



s1 = float(input("Enter marks for Subject 1: "))
s2= float(input("Enter marks for Subject 2: "))
s3 = float(input("Enter marks for Subject 3: "))


total = 300


obtained_marks = s1 + s2 + s3
percentage = (obtained_marks / total) * 100


if (s1 >= 33 and s2 >= 33 and s3 >= 33) and percentage >= 40:
    print("Congratulations! You have passed.")
else:
    print("Sorry! You have failed.")
