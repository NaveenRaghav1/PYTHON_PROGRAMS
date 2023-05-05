import random as r
name=input("enter your name please-->\n")
print('''
      -🙏🙏-------WELCOME-------🙏🙏-
                    ''')
print(name,'! Lets begin the game...😊😊 ')
print("-------------------------------------------")
num=r.randrange(1,10)
guess=100
i=0
score=0
while i<guess:
    guess_num=int(input("Guess the  number between 1 to 10 -->"))
    i+=1
    if guess_num<num:
        print("try again,your guess is low\n")
        
    if guess_num>num:
        print("try again,your guess is high\n")
    if guess_num==num:
        score+=10
        break
if num==guess_num:
     print(name,"You Won horray🎉🎉")
     print(name,f'you guess the number in {i} attempt')
     print("Your score is -->",score*i)
     