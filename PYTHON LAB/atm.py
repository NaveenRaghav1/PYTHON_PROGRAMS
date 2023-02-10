amt=int(input("enter the amount-"))
amt=amt-100

twok=amt//2000
amt%=2000
fiveh=amt//500
amt%=500
twoh=amt//200
amt%=200
oneh=amt//100

print("no.of 2000 notes are ",twok)
print("no.of 500 notes are ",fiveh)
print("no.of 200  notes are ",twoh)
print("no.of 100  notes are ",oneh+1)