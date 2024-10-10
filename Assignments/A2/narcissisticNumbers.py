'''
  Print and count the "Narcissistic Number"
'''
def findNarcissisticNums(start, end):
  numList = []

  # cycle through every integer within the specified range [start, end)
  for n in range(start, end):
    ones = n%10        # ones = the digit in the "ones" position of the integer
    tens = n//10%10    # tens = the digit in the "tens" position of the integer
    hundreds = n//100  # hundreds the digit in the "hundreds" position of the integer

    # calculate value of digits cubed and added up
    cubedDigits = ones**3 + tens**3 + hundreds**3  

    if cubedDigits == n:    # if the digits cubed then added up == n, then n is a narcissistic number.
      numList.append(str(n))  # append "n" to the list of narcissistic numbers

  return numList # return the list of narcissistic numbers

    
  
# run program until stopped by "QUIT" entry
while True:
  
  startIndex = input("Enter the starting integer, or QUIT to exit: ").strip().upper() # prompt user to enter the start of a range

  if startIndex == "QUIT": # if the user entered "QUIT", the program will stop.
    print("Quit program.")
    break
  
  endIndex = input("Enter the ending integer, or QUIT to exit: ").strip().upper() # prompt user to enter end of the range
  
  if endIndex == "QUIT":
    print("Quit program.")
    break

  if startIndex.isdigit() and endIndex.isdigit() and len(startIndex)==3 and len(endIndex)==3: # if the user enters a valid start/end 3-digit range
    
    narcissisticNumbers = findNarcissisticNums(int(startIndex), int(endIndex)) # call the function to find narcissistic Numbers

    # if there are numbers in the returned list
    if(narcissisticNumbers):
      print(f"The narcissistic numbers from {startIndex} (inclusive) to {endIndex} (exclusive) are: {", ".join(narcissisticNumbers)}")
    # if the returned list is empty
    elif(not narcissisticNumbers):
      print(f"There are no narcissistic numbers from {startIndex} (inclusive) to {endIndex} (exclusive).")

  else: # if the user inputs anything other than "QUIT", or two valid 3-digit numbers
    print("ERROR: Inputs must be 3-digit integers, try again.")