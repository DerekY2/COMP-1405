## Guessing Game program

import random

randomInt = random.randint(1,100)

for i in range(1,11):
  guess = int(input(f"Attempt #{i}: Guess a number between 1 to 100: "))
  if guess == randomInt:
    print(f"You are correct! The number was {randomInt}.") 
    break
  else:
    if guess < randomInt:
      print("Your guess was too low.")
    else:
      print("Your guess was too high.")
    if i==10:
      print(f"The correct number was {randomInt}.")