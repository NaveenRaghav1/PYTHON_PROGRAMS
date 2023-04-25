def name(a):
    """this programe is for enter the user name and doing small calculaations of additoion and substractions"""
    b=("hello "+a+ " i am vs code how i can help you-\n")
    print(b)
    c=("hi "+a+" you like playing some maths calculations--")
    print(c)
    d=input("type y for yes and n for no--")
    print(d)
    if d=='y':
        n=int(input("enter first number-->"))
        m=int(input("enter second number -->"))
        print("sum of the number is -->",n+m)
        print("subtract is ",n-m)
        print("thanks for using ...")  
    else:
        print("try again ...")
a=input("enter your name please -->")
name(a)
print(name.__doc__)#this is for print the docstinng which you make for readable the program and it is a string which is type inside the functoin
