principal=int(input("enter the principle of amount--"))
rate=int(input("enter the rate of the interst --"))
time=int(input("enter the time for amount --"))
sim_interest=(principal*rate*time)/100

total_amt=sim_interest+principal

print("interest of the amount is---",sim_interest)

print("total amount is---",total_amt)