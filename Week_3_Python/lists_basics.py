# List

# list are exactly what you expect. They are lists
# they are organised with index. This means it starts at 0

# syntax
# [] = list
print(type([]))
print([]) # just prints the brackets []
print(len([])) # counts the number of items in the list

# example
# defining a list and assigning it to a variable
contact_list = ['mike', 'kate', 'bell', 'kevin', 123, True]
#      index = [ 0  ,      1 ,     2,        3]

# changing the entire variable name
# you can use refractor to change entire variable name

# print all values on the list above
print(contact_list)
print(type(contact_list))  # prints the type which is list
print(type(contact_list[2])) # the type changes to string because you are accessing the data

# access one entry of the list
# use the index with the list
print(contact_list[2])
print(contact_list[-1])

# re-assigning an entry
print(contact_list)
contact_list[-2] = "Patrick"
print(contact_list)
contact_list[-1] = "Parent Hotel"

# to remove an entry from a list for example "Parent Hotel"
contact_list.pop() # put the number on the list
print(contact_list)

# list.pop(index = -1)
# add an entry to the list
contact_list.append('Filipe Paiva') # adds Filipe to the list
print(contact_list)

contact_list.append('kevin') # adds kevin to the list
print(contact_list)

# list.pop()
# remove entry and index 3
# what method?
# where in the documentation
contact_list.pop(2) # removes the 2nd item on the list

# list.remove(object)
# this only removes the first variable of that string even if there was two of the same name variables
contact_list.remove('kevin')
print(contact_list)


