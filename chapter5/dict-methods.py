a = {
   "key":"value",
   "harry":"code",
   "marks":"12",
   "list":[1,2,8]
   }


print(a.items()) #Output dict_items([('key', 'value'), ('harry', 'code'), ('marks', '12'), ('list', [1, 2, 8])])

print(a.keys()) # Output dict_keys(['key', 'harry', 'marks', 'list'])

print(a.values()) #output dict_values(['value', 'code', '12', [1, 2, 8]])

a.update({"key":"Srijita","marks":50}) # Update the dictionary because it is mutable

print(a) #Output {'key': 'Srijita', 'harry': 'code', 'marks': 50, 'list': [1, 2, 8]}


print(a.get("harry50")) # Output :none
print(a["harry50"]) # Output : Gives an error




# for more method (chatgpt)

# pop 

# popitem
