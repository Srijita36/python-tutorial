types=12
a= type(types)

print(a) # output : <class 'int'>


types=12.8
a= type(types)

print(a) # output : <class 'float'>

types="srijita"
a= type(types)

print(a) # output : <class 'str'>


# converting the type into another type === error


types="srijita"
a= type(types)

print(a) # output : <class 'str'>

b = "30"

c= int(b)

t=type(c)


print(t) # output : <class 'int'>