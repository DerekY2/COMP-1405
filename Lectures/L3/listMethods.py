### list methods
myList = [4, "Fred", 5, "Simon", 3, "Farah"]
index = 2
value = "New value"

print(myList,"\n")

# insert object to the end of the list 
myList.append(value)
print(f"{myList} - append(value)\n")

# insert object before specified index
myList.insert(index, value)
print(f"{myList} - insert(index, value)\n")

# remove first occurence of a value
myList.remove(value)
print(f"{myList} - remove(value)\n")

# return the value at index, then remove from list (used in functions - e.g. return list.pop(x) )
myList.pop(index)
print(f"{myList} - pop(index)\n")

# return the value at the end of the list, then remove from list (used in functions - e.g. return list.pop() )
myList.pop()
print(f"{myList} - pop()\n")

# removes all elements from list (empty list)
myList.clear()
print(f"{myList} - clear()\n")