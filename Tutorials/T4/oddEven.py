## check if integer input is even or odd

# while True:
#   try:
#     number = int(input("Enter an integer: "))
#   except ValueError:
#     print("Not a valid integer. Please try again.")
#     continue
#   else:
#     break

number = int(input("Enter an integer: "))

if number % 2 == 0: 
  print("Input is even.")
else:
  print("Input is odd.")