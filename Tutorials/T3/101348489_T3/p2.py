menu = ["Ice Cream", 3.67, 2, "Donuts", 2.50, 6, "Roll", 7.89, 3, "Pizza", 13.45, 5, "Fish and Chips", 15.20, 23, "Poutine", 8.51, 13, "Tacos", 3.00, 19]
foodItems = menu[::3]
prices = menu[1::3]
quantities = menu[2::3]
meanLength =0
quantConvert =[]

for j in foodItems:
        meanLength = meanLength + len(j)
meanLength = meanLength/(len(foodItems)+1)

for h in range(len(prices)):
        prices[h]=round(prices[h]*quantities[h],2)

for k in quantities:
        quantConvert.append(chr(k+64))

##output
print("The mean length of food items is: " + str(meanLength) + "\nMenu Order Summary: (Food Name: Price, Quantity)")
for l in range(len(foodItems)):
        print("         " + foodItems[l] + ": " + str(prices[l]) + ", " + str(quantConvert[l]))