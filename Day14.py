# Python Dictionary 
# In Python, a dictionary is a collection that allows us to store data in key: value pairs.

# 👉 Create a Dictionary 
# We create a dictionary by placing key-value pairs inside curly brackets {}.
# Example:
country_capital = {'India':'New Delhi', 'USA':'Washington, D.C', 'England':'London', 'Italy':'Rome'}
print(country_capital)
# Output:
# {'India': 'New Delhi', 'USA': 'Washington, D.C', 'England': 'London', 'Italy': 'Rome'}

# Note: Dictionary keys must be immutable, such as tuples, strings, integers, etc.
# We cannot use mutable (changeable) objects such as lists as keys.

# 👉 Python Dictionary Length
# We can get the size of a dictionary by using the len() function.
# Example:
country_capital = {'India':'New Delhi', 'USA':'Washington, D.C', 'England':'London', 'Italy':'Rome'}
print(len(country_capital))
# Output: 4

# 👉 Access Dictionary Items
# We can access the value of a dictionary item by placing the key inside square brackets.
# Example:
country_capital = {'India':'New Delhi', 'USA':'Washington, D.C', 'England':'London', 'Italy':'Rome'}
print(country_capital['India'])
print(country_capital['USA'])
print(country_capital.get('England'))
print(country_capital.get('Italy'))
# Output:
# New Delhi
# Washington, D.C
# London
# Rome

# Note: We can also use the get() method to access dictionary items.

# 👉 Change Dictionary Items
# Python dictionaries are mutable (changeable). We can change the value of a dictionary element by referring to its key.
# Example:
# Example:
country_capital = {'India':'New Delhi', 'USA':'Washington, D.C', 'England':'London', 'Italy':'Nepal'}
country_capital['Italy'] = 'Rome'
print(country_capital)
# Output:
# {'India': 'New Delhi', 'USA': 'Washington, D.C', 'England': 'London', 'Italy': 'Rome'}

# 👉 Add Items to a Dictionary
# We can add an item to the dictionary by assigning a value to a new key (that does not exist in the dictionary). 
# Example:
country_capital = {'India':'New Delhi', 'USA':'Washington, D.C', 'England':'London', 'Italy':'Rome'}
country_capital['Germany'] = 'Berlin'
# or
# country_capital.update({'Germany':'Berlin'})
print(country_capital)
# Output:
{'India': 'New Delhi', 'USA': 'Washington, D.C', 'England': 'London', 'Italy': 'Rome', 'Germany': 'Berlin'}

# Note: We can also use the update method() to add or change dictionary items.

# 👉 Remove Dictionary Items
# We use the del statement to remove an element from the dictionary. 
# Example:
country_capital = {'India':'New Delhi', 'USA':'Washington, D.C', 'England':'London', 'Italy':'Rome'}
del country_capital['USA']
# or
# country_capital.pop('USA')
print(country_capital)
# Output:
# {'India': 'New Delhi', 'England': 'London', 'Italy': 'Rome'}

# Note: We can also use the pop method() to remove an item from the dictionary.

# If we need to remove all items from the dictionary at once, we can use the clear() method.
# Example:
country_capital = {'India':'New Delhi', 'USA':'Washington, D.C', 'England':'London', 'Italy':'Rome'}
country_capital.clear()
print(country_capital)
# Output:
# {}

# Python Dictionary Methods
# pop() - Remove the item with the specified key.
# update() - Add or change dictionary items.
# clear() - Remove all the items from the dictionary.
# keys() - Returns all the dictionary's keys.
# values() - Returns all the dictionary's values.
# get() - Returns the value of the specified key.
# popitem() - Returns the last inserted key and value as a tuple.
# copy() - Returns a copy of the dictionary.

# 👉 Dictionary Membership Test
# We can check whether a key exists in a dictionary using the in operator.
dictionary1 = {1:"Hello", "Hi":24, "Howdy":100}
print(1 in dictionary1)

# the not in operator checks whether key doesn't exist
print("Howdy" not in dictionary1)
print("Python" not in dictionary1)
# Output:
# True
# False
# True

# 👉 Iterating Through a Dictionary
# A dictionary is an ordered collection of items (starting from Python 3.7).
# Meaning a dictionary maintains the order of its items. 
# We can iterate through dictionary keys one by one using a for loop.
country_capital = {'India':'New Delhi', 'USA':'Washington, D.C', 'England':'London', 'Italy':'Rome'}
# print dictionary keys one by one
for i in country_capital:
    print(i)
print("--------")
# print dictionary values one by one
for i in country_capital:
    print(country_capital[i])

# Output:
# India
# USA
# England
# Italy
# --------
# New Delhi
# Washington, D.C
# London
# Rome


