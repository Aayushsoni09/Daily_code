n=int(input("enter n"))
i=1

while i<=n:
    j=1
    c="A"
    while j<=i:
        print(c,end="")
        j=j+1
        c = chr(ord(c) + 1)
    print("")
    i=i+1
