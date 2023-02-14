side1=int(input("enter the first side of triangle- "))
side2=int(input("enter the second side of triangle- "))
side3=int(input("enter the third side of triangle- "))
#for isoscales triangle
'''if side1==side2:
    print("this is a isoscles triangle ")
elif side2==side3:
    print("this is a isoscles triangle ")
elif side1==side3:
    print("this is a isoscles triangle ")
else:
    print("invalid triangle")
    '''
if side1==side2 or side2==side3 or side1==side3:
    print("this is a isoscles trianle ")
#else:
   # print("invalid triangle")
    
#for right triangle
hyp=(side2**2)+(side3**2)
tri=side1**2
if hyp==tri:
    print("this is a right angled triangle")
#else:
    #print("invalid triangle")

#for scalene triangle
if side1!=side2 and side2!=side3 and side1!=side3:
    print("this is a scalene  trianle ")
#else:
    #print("invalid triangle")
