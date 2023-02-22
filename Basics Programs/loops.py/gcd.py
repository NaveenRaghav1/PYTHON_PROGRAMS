print("Enter Two Numbers: ")
numOne = int(input())
numTwo = int(input())

if numOne>numTwo:
    lcm = numOne
else:
    lcm = numTwo

while True:
    if lcm%numOne==0 and lcm%numTwo==0:
        break
    else:
        lcm = lcm - 1

print("\nLCM =", lcm)