n=32
l=len(bin(n)[2:])
for i in range(n+l):
    x=bin(i)[2:]
    print(" "*(l-len(x))+x)