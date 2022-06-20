
#Tuples are used to store multiple items in a single variable
#A tuple is a collection which is ordered and unchangeable.


thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Allow Duplicates

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple length

print(len(thistuple))

#one item add comma

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Example
#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)




