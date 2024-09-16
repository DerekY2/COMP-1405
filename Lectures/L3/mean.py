### find the average between elements in a list

numList = list(range(6))
total = 0

# add the value at each index to the total
for x in numList:
  total = total + x

# divide by the number of elements
average = total/len(numList)

print(f"The average of the list of numbers {numList} is {average}.")