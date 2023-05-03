import random as r
print("-------------------------------------------")
name=input("enter your name please-->\n")
print('''
      -🙏🙏-------WELCOME-------🙏🙏-
                    ''')
print(name,'! Lets begin the game...😊😊 ')
print("-------------------------------------------")
n=10
#pl_ch=input("enter your choice...(R for rock,S for scissor,W for water..)\n")
ls=['R','S','P']
com_ch=r.choice(ls)
for i in range(1,n):
    pl_ch=input("enter your choice...(R for rock,S for scissor,W for water..)\n")
    if pl_ch=='R'and com_ch=='S':
        print(name,'you won')
    elif pl_ch=='P'and com_ch=='R':
        print(name,'you won')
    elif pl_ch=='S'and com_ch=='P':
        print(name,'you won')
        
if pl_ch==com_ch:
    print("tie both choice is same..")
else:
    print("Computer won\n the choice of the computer is-->",com_ch)
 
        
        