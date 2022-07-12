n=int(input("enter n"))
i=1

while i<=n:
    j=1
    while j<=n:
        s=chr(ord("A")+i-1)
        print(s,end="")
        j=j+1
    print("")
    i=i+1