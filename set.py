Set={3,4,6,78,9}
print(Set)
# print a empty set and add the value in it

s=set()
s.add(30)
s.add(23)
s.add(1000)
s.add(34)
print(s)
#set methods
print(len(Set))

s.remove(30)#remove the element from the set
print(s)
print(s.pop())#remove the set element from indexing
print(s)
#unnion of sets
print(s.union(Set))
#print(s)
s1={20,40,5,60,7,51,}
s2={11,22,5,33,44}
#print(Set.union(s1,s2))
print(s1|s2)

#intersection of the set

print("intersection of the set is ",s1&s2)
s.clear()
print(s)
print(type(s1))