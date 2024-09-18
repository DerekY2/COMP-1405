firstName = "John"
lastName = "Deere"
fullName = firstName + lastName
print(fullName)

string1 = "   lots of random whitespaces idk  "
print(string1.strip())
print(string1.strip("wca."))

print(string1.split())
print(string1.split("o"))

print(string1.split(maxsplit=2))

print(' '.join(string1.split()))
print(':'.join(string1.split()))