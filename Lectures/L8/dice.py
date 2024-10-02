import random

while True:
  numDiceStr = input("Enter the number of dice to roll or exit ti quit: ")
  if numDiceStr.upper()=="EXIT":
    break
  numDiceInt = int(numDiceStr)
  for die in range(numDiceInt):
    faceValue = random.randint(1,6)
    print(f"Die value is {faceValue}")