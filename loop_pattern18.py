n=int(input("enter n"))
i=1

while i<=n:
    j=1
    c=i
    while j<=i:
        print(chr(ord("A")+c-1),end="")
        j=j+1
        c=c+1
    print("")
    i=i+1