amt=int(input("enter the total shopping amount= "))
if amt>25000:
    print("category is GOLD")
    disc=(20*amt)/100
    print("Amount to be paid=",amt-disc)
elif amt>=10000 and amt<=25000:
    print("category is SILVER")
    disc=10*amt/100
    print("Amount to be paid=",amt-disc)
else:
    print("category is BRONZE")
    disc=5*amt/100
    print("Amount to be paid=",amt-disc)
