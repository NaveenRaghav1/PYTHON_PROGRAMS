#no of tiles required in a floor

flen=int(input("enter lenght of the floor-"))
fbdth=int(input("enter breadth of the floor-"))

tlen=int(input("enter lenght of the tiles-"))
tbdth=int(input("enter breadth of the tiles-"))

area_f=flen*fbdth
area_t=tlen*tbdth

tiles=-(-area_f//area_t)
print("no of tiles required in the floor ---",tiles)