n=int(input("enter no of rows--"))
bool=input("enter boolean expression in True/False--->")
if bool=='True' or bool=='true' or bool=='1' :
    for i in range(n+1):
        #for j in range(1,i+1):
        print('*'*i,end='')
        print()
if bool=='False' or bool=='false' or bool=='0':
    for i in range(n):
        #for j in range(n-i):
          print('*',end='')
    print()
        