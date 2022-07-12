n=int(input("enter n"))
i=1

while i<=n:
    space=n-i
    j=1
    while space:
        print(" ",end="")
        space=space-1
    while j<=i:
        print(j,end="")
        j=j+1


    k=i-1
    while k>i-j+1:
        print(k,end="")
        k=k-1

    print("")
    i=i+1