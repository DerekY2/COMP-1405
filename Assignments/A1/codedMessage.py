## translate the user's input in a coded message
message = input("Enter a message to be encoded:\n")
shift = int(input("Enter an integer value between 1-5 (inclusive): "))
shiftedMessage = []

# i. convert string to uppercase letters
message = message.upper()

# ii. apply Caesar cipher; iii. non-alphabetic characters remain unchanged
# cycle through every character in the message
for character in message:
  # find the ASCII code of the character
  code = ord(character)
  # if the character's code is greater or equal to 65(A)
  if code>=65:
    # up to the selected shift amount
    if code<=90-shift:
      character = chr(code+shift) # shift the letter down by the selected shift amount
    # up to Z(90)
    elif code<=90:
      character = chr(code+shift-26) # map the letters back to start of the alphabet after the shift
  # append the shifted letter or unshifted character to a list
  shiftedMessage.append(character)

# join the list into a string message
shiftedMessage = str(''.join(shiftedMessage))

# display coded message
print(f"The coded message is: \n{shiftedMessage}")