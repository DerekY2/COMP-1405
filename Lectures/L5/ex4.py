name = input("Enter your name:\n").strip()

outputStr = "No name was entered"
if(name):
  outputStr = "Your name is " + name + "."

print(outputStr)