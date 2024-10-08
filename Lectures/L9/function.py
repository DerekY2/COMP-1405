## Quadratic formula function
def findRoots(a, b = 0, c = 0):
  discriminant = (b**2)-(4*a*c)
  # check if discriminant is greater, less or equal to zero
  if discriminant > 0:
    # two roots
    root1 = (-b + discriminant**.5)/(2*a)
    root2 = (-b - discriminant**.5)/(2*a)
    return root1, root2
  elif discriminant == 0:
    # one root (repeating)
    root = -b/2*a
    return root
  else:
    # discriminant < 0, no real roots
    return None
  
print(findRoots(3,2,-1))