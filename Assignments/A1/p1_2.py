myList = ["tiger", 4, "buffalo", 6, "horse", 8, "cat", 1, 2, 50, 60, 3, 70, 80, 5, 100]
substring = myList[2].strip("buo")
substring
greaterList = myList[13:16:2]
greaterList
primeNumList = myList[8:15:3]
primeNumList
animalList = myList[:7:2]
animalList
primeNumList = []
primeNumList2 = []
primeIndexList = []
greaterList = []

primeNumList = myList[8:15:3]
primeNumList

greaterList = myList[13:16:2]
print(greaterList)

substring = myList[2].strip("buo")
print(substring)

# for x in myList:
#   isPrimeNum = True
#   if type(x)==int and x!=1!=0:
#     for n in range(2, x): 
#       if x%n==0: ## as soon as x is divisable by integer n, we know it is not a prime number.
#         isPrimeNum = False
#         break
#     if isPrimeNum:
#       primeNumList.append(x)
# print(primeNumList)

# # for y in range(len(myList)):
# #   isPrimeNum = True
# #   if type(myList[y])==int and myList[y]!=1!=0:
# #     for n in range(2, myList[y]):
# #       if myList[y]%n==0: ## as soon as x is divisable by integer n, we know it is not a prime number.
# #         isPrimeNum = False
# #         break
# #     if isPrimeNum:
# #       primeIndexList.append(y)
# # for index in primeIndexList:
# #   primeNumList2.append(myList[index])
# #   print(primeNumList2)
