a=int(input())
b=int(input())
c=int(input())
out=a if a>b and a>c else b if b>c and b>a else c #using single line if else
print("greatest is --",out)