# COMP 1005/1405 Section E - Assignment 2
''' Project Details
            Name: Derek Yu
            Student #: 101331395
            Date Created: Oct. 09 2024

            Generates a pseudo-random number, and determines whether it is a prime number or not
'''

import random

# same function from Part II Q1
def findDivisors(number):
  divisors=[]

  # cycle through every integer form 0 to "number", inclusive
  for i in range(1, number + 1):

    # determine if 'i' is a divisor
    if number % i == 0: 
      divisors.append(str(i))
  return divisors

#  generate a number between 1-30(inclusive)
number = random.randint(1,30)
print(f"The generated number is: {number}")

# determine if it is a prime number (has <3 divisors)
if number!=1 and len(findDivisors(number))<3:
  print("This is a prime number!")
else:
  print("This is not a prime number.")