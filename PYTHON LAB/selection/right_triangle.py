#wap to find the triangle is right or not with the given three sides
s1=int(input())
s2=int(input())
s3=int(input())
out=s1 if s1>s2 and s1>s3 else s2 if s2>s3 and s2>s1 else s3
if (out)**2==s1**2+s2**2+s3**2-(out)**2:
    print("it is right triangle")
else:
    print("not a right triangle")
    