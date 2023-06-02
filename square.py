n=int(input())
for i in range(1,n+1):
    if i==1 :
        print("*"*n)
    for j in range(i):
        if j==1 or j==n:
            print("*")
for i in range(n-i+1):
    print(' ',end='')
    if i==n:
        print("*")
#incomplete..............🤨🤨🤨🤨🤨