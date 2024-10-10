n = 9
divisors=[]
for i in range(1,n//2+1):
  if n%i==0:
    divisors.append(str(i))

dvd = ", ".join(divisors)

print(f"n = 9 has divisors: {dvd} and {n}.")