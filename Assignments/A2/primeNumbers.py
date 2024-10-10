'''
  - Generate and display a pseudo-random number within the range [1,30],
    then determine whether it is a prime number of not.
  - Implements the findDivisors() function from Part II Q1
'''

import random
import divisors # we can simply import the divisors.py file from Part II Q1. However the function itself is still included in this file just in case divisors.py is inaccessible to the person marking this assignment

number = random.randint(1,30)
print(f"The generated number is: {number}")
if number!=1 and len(divisors.findDivisors(number))<3:
  print("This is a prime number!")
else:
  print("This is not a prime number.")