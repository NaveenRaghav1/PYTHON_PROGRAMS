n=int(input("enter number "))
m=int(input("enter number "))
o=(input("enter number "))

if n>m:
    print("n is greatest--")
elif m>0:
    print("m is greatest--")
else:
    print("o is greatest")
try:
    print("the sum of the number is",n+m)
    int(n)+int(o)
except Exception as e:
    print(e)        #it print the error as usual 
    