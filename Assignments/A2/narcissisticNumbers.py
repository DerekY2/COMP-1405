''' 
  COMP 1005/1405 Section E - Assignment 2 Part II Q2
  Project Details
      Name: Derek Yu
      Student #: 101331395
      Date: October 15, 2024
  
  External Libraries Used
      None
  
'''

def findNarcissisticNums(start, end):
  """
  Function Description:
    Find all narcissistic numbers within a range
  Parameters:
    start (int): start of range (inclusive)
    end (int): end of range (exclusive)
  Return:
    numList (list): list of all narcissistic numbers in range [start,end)
  """
  numList = []
  # cycle through every integer within the specified range [start, end)
  for n in range(start, end):
    # split each integer into its digits
    ones = n%10
    tens = n//10%10
    hundreds = n//100
    cubedDigits = ones**3 + tens**3 + hundreds**3  

    if cubedDigits == n:  
      numList.append(str(n))  # n is a narcissistic number, append to list
  return numList

# run program until stopped by "QUIT" entry
while True:
  startIndex = input("Enter the starting integer, or QUIT to exit: ").strip().upper()
  if startIndex == "QUIT": # handle user quit request
    print("Quit program.")
    break

  endIndex = input("Enter the ending integer, or QUIT to exit: ").strip().upper()
  if endIndex == "QUIT":
    print("Quit program.")
    break

  # check if user entered a valid 3-digit range
  if len(startIndex)==3 and len(endIndex)==3 and startIndex < endIndex: 

    # determine narcissistic numbers in the range
    narcissisticNumbers = findNarcissisticNums(int(startIndex), int(endIndex))
    if(narcissisticNumbers):
      print(f"The narcissistic numbers from {startIndex} (inclusive) to {endIndex} (exclusive) are: {", ".join(narcissisticNumbers)}")
    elif(not narcissisticNumbers):
      print(f"There are no narcissistic numbers from {startIndex} (inclusive) to {endIndex} (exclusive).")
  
  else: # if the user inputs anything other than "QUIT", or two valid 3-digit numbers
    print("ERROR: Inputs must be a valid range of 3-digit integers, try again.")