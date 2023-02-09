'''def swap(l):
    size=len(l)
    temp=l[0]
    l[0]=l[size-1]
    l[size-1]=temp
    return l
l = [12, 35, 9, 56, 24]
p1=int(input())
print(swap(l))
'''
def swap(f):
    size=len(f)
    temp=f[0]
    f[0]=f[size-1]
    f[size-1]=temp
    return f
f='hello'
list(f)
print(swap(f))