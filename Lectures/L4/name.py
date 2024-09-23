firstName = "John"
lastName = "Deere"
fullName = firstName + lastName
print(fullName)

string1 = "br.   lots of random whitespaces idkbr  .br"
print(string1.strip())
print(string1.strip("br."))

print(string1.split())
print(string1.split("o"))

print(string1.split(maxsplit=2))

print(' '.join(string1.split()))
print(':'.join(string1.split()))

print(string1.find("lots"))
print(string1.find("random"))
print(string1.find("zzz"))

print(string1[5:15])