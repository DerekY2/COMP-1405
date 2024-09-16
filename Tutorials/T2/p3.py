bill = float(input("Enter the bill amount: "))
tipPercentage = float(input("Enter the tip percentage: "))
tip = bill*(tipPercentage/100)
print(f"A {tipPercentage}% tip on a ${bill} bill equals ${tip}\nThe total bill is: ${bill+tip}")