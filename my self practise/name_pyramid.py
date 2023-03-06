c=1
n=10
s="NAVEEN_RAGHAV"
l=len(s)
k=n*(n+1)//2
for i in range (k):
    
    x=c*(c+l)//2
    if i==x:
        print()
        print(s[i%l],end="")
        c+=1
    else:
        print(s[i%l],end=" ")
        

