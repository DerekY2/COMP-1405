'''
  Part II Q1
  Write a function that takes an integer input and returns a list of its divisors as output
'''

# take an integer as in input
def findDivisors(number):
  divisors=[]
  
  # cycle through every integer form 0 to "number", inclusive
  for i in range(1, number + 1):

    # if number%i ==0, it is a divisor of "number"
    if number % i == 0: 
      divisors.append(str(i)) # append the divisor to the list of divisors

  return divisors # return list of divisors

# print(findDivisors(90))