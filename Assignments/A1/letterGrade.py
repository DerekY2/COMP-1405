# Generate a letter grade based on the user's input value
score = float(input("Enter a real value score between 0.0 and 1.0: "))

# print error message if score is less than 0 or greater than 1
if score <0.0 or score > 1.0:
  print("ERROR: Score must be between 0.0 and 1.0")
# Go through every letter grade until corresponding range is attained
elif score >= 0.9:
  print("Letter grade: A") 
elif score >= 0.8:
  print("Letter grade: B")
elif score >= 0.7:
  print("Letter grade: C")
elif score >= 0.6:
  print("Letter grade: D")
# any grade below 0.6 corresponds to letter grade F
else:
  print("Letter grade: F")