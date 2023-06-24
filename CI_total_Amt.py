principal=int(input("enter the principle of amount--"))
rate=int(input("enter the rate of the interst --"))
time=int(input("enter the time for amount --"))

com_interest=principal*(1+rate/100)**time-principal

total_amt=com_interest+principal

print("interest of the amount is---",com_interest)

print("total amount is---",total_amt)