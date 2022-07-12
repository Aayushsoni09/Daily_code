n=int(input("enter n"))
i=1
c=1
while i<=n:

    space=n-i
    j=1
    while space:
        print(" ",end="")
        space=space-1
    while j<=i:

        print(c,end="")
        j=j+1
        c=c+1
    print("")
    i=i+1