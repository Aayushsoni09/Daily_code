n=int(input("enter n"))
i=1
c="A"
while i<=n:
    j=1
    while j<=i:
        print(c,end="")
        j=j+1
        c=chr(ord(c)+1)
    print("")
    i=i+1