fur = input("Does your animal have fur").upper()
feather = input("Does your animal have feathers").upper()
egg = input("Does your animal fertilize eggs exteriorly?").upper()
gill = input("Does your abimal have gills").upper()

if(fur == "YES"):
  print("mammal")
else:
  if(feather == "YES"):
    print("bird")
  else:
    if(egg == "YES"):
      if(gill =="YES"):
        print("fish")
      else:
        print("")