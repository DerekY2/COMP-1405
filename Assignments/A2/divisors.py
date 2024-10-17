''' 
  COMP 1005/1405 Section E - Assignment 2 Part II Q1
  Project Details
      Name: Derek Yu
      Student #: 101331395
      Date: October 15, 2024
  
  External Libraries Used
      None
    
'''

# Function that returns a list of divisors of "number"
def findDivisors(number):
  """
  Function Description:
      Finds all divisors of a number
  Parameters:
      number (int): a number
  Return:
      list: list of divisors of number
  """
  divisors=[]
  # Find all integer divisors
  for i in range(1, number + 1):
    if number % i == 0: 
      divisors.append(str(i)) # "i" is a divisor, so we append it to the list of divisors
  return divisors