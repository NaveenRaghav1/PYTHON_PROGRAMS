#to find the hypotenuse side of the right angled triangle

base=int(input("enter the base of the triangle -"))
height=int(input("enter the height of the triangle -"))

 #using math module.....
import math
hyp=(base*base)+(height*height)
print(math.sqrt(hyp)) 

#without using math module
hyp_Side=hyp**(1/2)
print("the hypotenuse side of the triangle is-- ",hyp_Side)

