## determine if integer input is less/greater than or equal to zero

# while True:
#   try:
#     number = int(input("Enter an integer: "))
#   except ValueError:
#     print("Not a valid integer. Please try again.")
#     continue
#   else:
#     break

number = int(input("Enter an integer: "))

if number > 0:
  print("Input is greater than 0.")
else:
  if number < 0:
    print("Input is less than 0.")
  else:
      print("Input is equal to 0.")