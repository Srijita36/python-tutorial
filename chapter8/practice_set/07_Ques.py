# Write a python function to remove a given word from a list ad strip it at the same 
# time.

def rem(list,word):

    for item in list:

        list.remove(word)

        return list

        

list=["ram","riya","puja","sam"]

print(rem(list,"sam")) # OutPut Is ['ram', 'riya', 'puja']





def rem(list,word):

    n=[]

    for item in list:

        
        if not (item==word):
            n.append(item.strip(word))

    return n

        

list=["ram","rohan","puja","an"]

print(rem(list,"an")) # OutPut Is ['ram', 'roh', 'puj']