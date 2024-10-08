'''
  Generate a multiplication table from 1-9
'''

number = int(input("Enter a number between 1-9: "))

for y in range(1, number+1):    # for every integer from 1-number (y)
  for x in range(1, number+1):    # for every integer from 1-number (x)
    print(x*y, end="\t")            # multiply (y) with every value of (x) and print, seperated by \t
  print("")                       # row is completed. Return a new line, and move on to next value of (y)