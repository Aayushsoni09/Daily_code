n=int(input("enter n"))
i=1

while i<=n:
    space=0
    j=1
    while space<i-1:
        print(" ",end="")
        space=space+1
    while j<=n-i+1:
        print("*",end="")
        j=j+1
    print("")
    i=i+1