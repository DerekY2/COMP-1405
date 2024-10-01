A=B=E=H=K=False
C=D=F=G=I=J=L=True
X=(((((not G) and F) or C) or E) or (not D) and H) or ((not A) and (not B))
print(X)

C=E=G=H=I=K=False
A=B=D=F=J=L=True
X = ((((not A) and (not F)) or (C and B) or D) and (not E)) and H or G
print(X)
