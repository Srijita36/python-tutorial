
# Ques-1 > Write a program to print Twinkle Twinkle little star poem in python.

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')


# Ques-2 > Use REPL and print the table of 5

# Ques-3 > Install an external module and use it to perform an operation of you interest.

import pyttsx3

my= pyttsx3.init()
my.say("")
my.runAndWait()


# Ques-4 > Write a python program to print the contents of a dictonary using the os modules.

import os

# Select the directory whose content you want to list 
directory_path = '/Users\SRIJITA\OneDrive\Documents\Data Analyst\Python'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)

