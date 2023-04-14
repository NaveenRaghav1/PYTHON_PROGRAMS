#mini calc using if elif-else
n1=int(input("enter the first number--"))
n2=int(input("enter the second number--"))
op=input("enter the valid operators like--> +,-,/,*....>")
if op=='+':
    print("the sum is -",n1+n2)
elif op=='-':
    print("the subtraction id -",n1-n2)
elif op=='/':
    print("the division of the number is-",n1/n2)
elif op=='*':
    print("the multiplication is --",n1*n2)
else:
    print("enter valid operator..")
    print("thank you ")