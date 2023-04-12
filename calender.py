
n=int(input())
if n==28:
    print("month is feb")
elif n==30:
    print("month is april,june,sep,november")
elif n<=31:
    print("month is jan,march,may,july,aug,oct,dec")
elif n>31:
    print("month not lie in the calender")
else:
    print("thanks you")
