n=int(input("enter n"))
c=0
while n!=0:

    if n&1==0:
        c+=1
    n=n>>1
print(c)
