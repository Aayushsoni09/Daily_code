n=int(input("enter n"))
i=1

while i<=n:
    space=n-i
    j=1
    while space:
        print(" ",end="")
        space=space-1
    while j<=i:
        print(i,end="")
        j=j+1
    print("")
    i=i+1