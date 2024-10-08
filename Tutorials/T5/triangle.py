## Number Pyramid
rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1): # rows+1 = number of lines needed
  for j in range(i): # print the integer "i", "i" number of times
    print(i, end="")
  print("") # go to next line after each run