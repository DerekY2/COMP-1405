i = 18
b = True

while b:
  print(i)
  i+=5
  if i>98:
    b=False

while b:
  print(i)
  i+=5
  if i>98:
    break

thing = 3.134534
print(f"{thing: .3f}")
print(f"{round(thing, 4)}")
print(f"{round(thing,4)}")

def ask(q):
  return input(q).upper()
# if ask("Does \"this\" work: ") == "Y":
#   print("It indeed works")
# else:
#   print("No workey :(")


if ask("Is it 1")=="Y":
  print("Yes it is 1")
elif ask("Is it 2")=="Y":
  print("Yes it is 2")
elif ask("Is it 3")=="Y":
  print("Yes it is 3")
elif ask("Is it 4")=="Y":
  print("Yes it is 4")
else:
  print("It is 5")