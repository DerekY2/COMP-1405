'''
  - Generate and display a pseudo-random number within the range [1,30],
    then determine whether it is a prime number of not.
  - Implements the findDivisors() function from Part II Q1
'''

import random
import divisors

number = random.randint(1,30)
print(f"The generated number is: {number}")
if number!=1 and len(divisors.findDivisors(number))<3:
  print("This is a prime number!")
else:
  print("This is not a prime number.")