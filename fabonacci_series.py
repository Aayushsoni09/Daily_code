n=int(input("enter n"))
a=0
b=1
print(a)
print(b)

for i in range(n):
    nextnum=a+b
    print(nextnum)
    a=b
    b=nextnum
