name=input("enter your name please--\n")
a=int(input("enter first number--"))
b=input("enter the operator like(*,+,-,/,%)--")
c=int(input("enter second number--"))
if b=="+":
    print("the sum is ",a+c)
elif b=="-":
    print("the difference is ",a-c)
elif b=="*":
    print("the multipication  is ",a*c)
elif b=="/":
    print("the difference is ",a/c)
else:
    print("enter valid operators--")
print("thank you for using "+name)
