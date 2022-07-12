n=int(input("enter n"))
i=1
c="A"
while i<=n:
    j=1
    while j<=n:
        print(c,end="")
        c=chr(ord(c)+1)
        j=j+1
    print("")
    i=i+1