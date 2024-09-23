name = "John Deere"
a = ":3"
b = 0
for x in name:
  num = ord(x)
  print(num)
  for y in range(num):
    print(f"{a} {y}")