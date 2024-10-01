## 2a.
menu = ["Ice Cream", 3.67, 2, "Donuts", 2.50, 6, "Roll", 7.89, 3, "Pizza", 13.45, 5, "Fish and Chips", 15.20, 23, "Poutine", 8.51, 13, "Tacos", 3.00, 19]
foodItems = menu[0::3]
prices = menu[1::3]
quantities = menu[2::3]
totalLength=0
totalPrices=[]
convertedQuantities=[]
## 2b.

for x in foodItems:
  totalLength = totalLength + len(x)
meanLength = totalLength//len(foodItems)

## 2c.
for x in range(len(prices)):
  totalPrices.append(round(prices[x] * quantities[x], 2))

## 2d.
for x in range(len(quantities)):
  # print(quantities[x]+64,chr(quantities[x]+64),ord(chr(quantities[x]+64)))
  convertedQuantities.append(chr(quantities[x]+64))

## 3a. 
print(f"The mean length of the item names is {meanLength}\nMenu Order Summary: (Food Name: Price, Quantity)")
for x in range(len(foodItems)):
  print(f"    {foodItems[x]}: {totalPrices[x]}, {convertedQuantities[x]}")

  