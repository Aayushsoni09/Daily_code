n=int(input("enter n"))
i=1

while i<=n:
    j = 1
    while j<=n:
        c=ord("A")+i+j-2
        print(chr(c),end="")
        j=j+1
    print("")
    i=i+1