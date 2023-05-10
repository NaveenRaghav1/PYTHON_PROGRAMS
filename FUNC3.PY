def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("the greater number is -",num1)
    #elif num1>num3:
       # print("the greater number is -",num1)
    elif num2>num3 :
        print("the greater number is -",num2)
 
    else:
        print("the greater number is --",num3)
        
a=int(input())
b=int(input()) 
c=int(input())
max(a,b,c)       