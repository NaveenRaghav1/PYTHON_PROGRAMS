#right downward triangle pattern
n=int(input("enter no of rows--"))
for i in range(n):
     for j in range(1,n-i):
            print(' ',end="")
     for k in range(1,i+1):
         print("*",end="")
     print()
     #not completed