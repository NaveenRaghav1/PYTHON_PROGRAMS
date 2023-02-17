m=int(input("enter marks="))
match m:
    case m if m>90:
        print("O")
    case m if m>80:
        print("A+")
    case m if m>70:
        print("A")
    case m if m>60:
        print("B+")
    case m if m>50:
        print("B")
    case m if m>40:
        print("C") 
    case _:
        print("fail....")
               
        
        