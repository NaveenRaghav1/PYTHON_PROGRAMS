print("Printing current number and previous number sum in range(10)\n")
prev=0
for i in range(1,11):
    sum=prev+i
    print("current number",i,"previous number ",prev,"sum is ",sum)
    
    prev=i