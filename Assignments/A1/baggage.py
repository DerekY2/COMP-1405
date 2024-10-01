## Calculate baggage charges & total charges of a passenger
standardRate = 120.0 # standard rate for flight ticket
totalCharges = standardRate # total charges
baggageCharges = 0.0 # baggage charges


while True:
  # prompt user to enter baggage weight, then attempt to convert input to float
  try:
    weight = float(input("Enter total baggage weight: "))
  # if an error occurs(not int/float input), prompt user for input again
  except ValueError: 
    print("Error: Weight must be a number.")
    continue
  # if input is a valid number, exit loop
  else:
    break

# if weight is over 20kg
if(weight>20.0):
  # baggage charges equals to the additional weight(over 20kg) multiplied by 1.5% of the standard rate
  baggageCharges = (weight-20.0)*(standardRate*0.015)
  # set the total charges to include the baggage charges
  totalCharges = totalCharges + baggageCharges

# print standard rate, baggage charges, total charges
print(f"Standard rate: {standardRate}\nBaggage charges: {round(baggageCharges, 2)}\nTotal charges: {round(totalCharges, 2)}")