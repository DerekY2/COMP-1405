### reverse the order of elements in a list

nums = list(range(6))
reverseNums = []

print(nums)

for x in nums:
  print(f"value of x is {x}")
  reverseNums.insert(0,x)
  print(f"Building new list {reverseNums}")

print(reverseNums)