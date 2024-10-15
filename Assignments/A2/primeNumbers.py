# COMP 1005/1405 Section E - Assignment 2
''' Project Details
            Name: Derek Yu
            Student #: 101331395
            Date Created: Oct. 09 2024
    
    External Librairies Used
            findDivisors(number) - from Part II Q1
'''

import random

# take an integer as in input
def findDivisors(number):
  divisors=[]
  
  # cycle through every integer form 0 to "number", inclusive
  for i in range(1, number + 1):

    # if number%i ==0, it is a divisor of "number"
    if number % i == 0: 
      divisors.append(str(i)) # append the divisor to the list of divisors

  return divisors # return list of divisors


#  generate a number between 1-30(inclusive)
number = random.randint(1,30)
print(f"The generated number is: {number}")

# if findDivisors(number) returns 2 divisors, they must
# be 1 and the number itself, therefore "number" is a prime number.
# However 1 isn't a prime number.
if number!=1 and len(findDivisors(number))<3:
  print("This is a prime number!")
# more than 2 divisors, so it is not a prime number
else:
  print("This is not a prime number.")