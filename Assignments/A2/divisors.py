# COMP 1005/1405 Section E - Assignment 2
''' Project Details
            Name: Derek Yu
            Student #: 101331395
            Date Created: Oct. 09 2024
            
            A function which returns a list of divisors for a given number
'''

# Function that returns a list of divisors of "number"
def findDivisors(number):
  divisors=[]

  # Find all integer divisors
  for i in range(1, number + 1):

    if number % i == 0: 
      divisors.append(str(i)) # "i" is a divisor, so we append it to the list of divisors

  return divisors