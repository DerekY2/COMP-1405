rice = 0
cost = 1

rice2=0
cost2 = 1
square = 0

for _ in range(64): ## "_" signifies a placeholder for a value that will not be used as variable (save memory space)
  rice = rice + cost
  cost = cost*2

print(f"Number of grains of rice is {rice}")

while square < 64:
  rice2 = rice2 + cost2
  cost2 = cost2*2
  square = square+1

print(f"Number of grains of rice is {rice}")