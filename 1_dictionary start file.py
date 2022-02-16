
phonebook = {'Chris':'555−1111', # key -- value 
             'Katie':'555−2222',
             'Joanne':'555−3333'}
'''
print()
print('*****  start section 1 - print dictionary ********')
print()

#print(phonebook)
#print(type(phonebook))

# give key rather than index to get value (Chris's phone number)
#phone = phonebook['Chris'] 
#print(phone)

#print number of elements in phonebook dictionary
#print(len(phonebook)) 

#mydictionary = dict(m=8,n=9)
#print(mydictionary)

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chris'

#in function looks for a matching key in the dictionary 
#if Chris is a key in the phonebook, print the value (Chris's phone number)
if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not in the phonebook")


print()
print('*****  end section 2 ********')
print()





#keys are not immutable, if key does not exist it is added to dictionary

print()
print('*****  start section 3 - edit/append dictionary ********')
print()

#adding chris creates chris key and value in dictionary, changing Chris value updates value
print(phonebook)
phonebook['chris'] = '555-0123'

phonebook['Chris'] = '555-4444'
print(phonebook)



print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del command removes entire key value pair
del phonebook['Chris']

print(phonebook)



print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys ********')
print()

#prints keys from dictionary
for k in phonebook:
    print(k)
#prints values    
    print(phonebook[k])

print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - iterate through values  ********')
print()

#iterates through values
for value in phonebook.values():
    print(value)


print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

# .items() gives key/value pair as a tuple
for phonebook_tuple in phonebook.items():
    print(phonebook_tuple)

#splits key and value into seperate items
for key,value in phonebook.items():
    print(key)
    print(value)

print()
print('*****  end section 7 ********')
print()









print()
print('*****  start section 8 - using get and clear ********')
print()

#.get() in dictionary avoids key value error
phone = phonebook.get('chris','key not found')
print(phone)

#clears dictionary .clear()
phonebook.clear()
print(phonebook)

print()
print('*****  end section 8 ********')
print()


print()
print('*****  start section 9 - using pop method ********')
print()

#.pop() pops out a single key/value pair from dictionary
remove = phonebook.pop('Chris', 'key not found')
print(remove)

print(phonebook)

print()
print('*****  end section 9 ********')
print()


print()
print('*****  start section 10 - using pop item ********')
print()

#picks item to remove, always pops last item ('random')
a = phonebook.popitem()

print(a)
print(phonebook)

print()
print('*****  end section 10 ********')
print()



import random
print()
print('*****  start section 11 - using random and converting list ********')
print()


#creates a list of all the keys in dictionary, allowing for random function to be used
#random.choice selects one of the keys from the dictionary that has been converted into a list of the keys
randomPhone = phonebook[random.choice(list(phonebook))]

print(randomPhone)

print()
print('*****  end section 11 ********')
print()

'''