
n = int(input("enter n"))
i=0
answer=0
while n!=0:
    bit=n&1
    answer=(bit*pow(10,i))+answer

    n=n>>1
    i+=1
print(answer)