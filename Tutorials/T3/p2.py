## 2a.
menu = ["Ice Cream", 3.67, 2, "Donuts", 2.50, 6, "Roll", 7.89, 3, "Pizza", 13.45, 5, "Fish and Chips", 15.20, 23, "Poutine", 8.51, 13, "Tacos", 3.00, 19]
foodItems = menu[0::3]
prices = menu[1::3]
quantities = menu[2::3]

## 2b.
totalLength = 0
for x in foodItems:
  totalLength = totalLength + len(x)
  #print(x+str(len(x)))

meanLength = totalLength//len(foodItems)
print(meanLength)

## 2c.
totalPrices = prices[:]
for x in prices:
  currentIndex = prices.index(x)
  totalPrices[currentIndex] = round(prices[currentIndex] * quantities[currentIndex], 2)
  
print(totalPrices)

## 2d.
convertedQuantities = quantities[:]
for x in quantities:
  currentIndex = quantities.index(x)
  print(x+64,chr(x+64),ord(chr(x+64)))
  convertedQuantities[currentIndex] = chr(x+64)

print(convertedQuantities)

## 3a. 
print(f"The mean length of the item names is {meanLength}")
print(f"Menu Order Summary: (Food Name: Price, Quantity)")
for x in range(len(foodItems)):
  print(f"    {foodItems[x]}: {totalPrices[x]}, {convertedQuantities[x]}")