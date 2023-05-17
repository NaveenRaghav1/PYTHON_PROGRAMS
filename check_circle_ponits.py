c1=int(input("enter first point of centre-"))
c2=int(input("enter second point of centre-"))
p1=int(input("enter first point of x,y plane-"))
p2=int(input("enter first point of x,y plane-"))

radius=int(input("enter the radius of the circle --"))
centre=(input(" the centre of the circle is( %d %d)"%(c1,c2) ))
point=(input("the points in X,Y-plane is (%d %d)"%(p1,p2)))

dist=(c1-p1)**2+(c2-p2)**2
d=dist**1/2

if d>radius:
    print("points lies outside the circle")
else:
    print("points lies inside the circle")