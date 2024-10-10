'''
  - Generate and display a pseudo-random number within the range [1,30],
    then determine whether it is a prime number of not.
  - Implements the findDivisors() function from Part II Q1
'''

import random
import divisors # import function findDivisors()

#  generate a number between 1-30(inclusive)
number = random.randint(1,30)
print(f"The generated number is: {number}")

# if findDivisors(number) returns 2 divisors, they must
# be 1 and the number itself, therefore "number" is a prime number.
# However 1 isn't a prime number.
if number!=1 and len(divisors.findDivisors(number))<3:
  print("This is a prime number!")
# more than 2 divisors, so it is not a prime number
else:
  print("This is not a prime number.")