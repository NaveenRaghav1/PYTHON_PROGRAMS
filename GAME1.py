#game between two players ---stone,scissors,paper

p1=input("enter the name -->")
c1=input("enter the choice --stone,paper scissor--> ")
p2=input("enter the name -->")
c2=input("enter the choice --stone,paper scissor--> ")

if (c1== 'stone' and c2=='paper') or (c1=='scissor' and c2=='paper') or (c1=='stone' and c2=='paper'):
    print("winner is =",p1)
else:
    print("winner is =",p2)