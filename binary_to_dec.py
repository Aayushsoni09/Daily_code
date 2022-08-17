
n = int(input("enter n"))
i=0
answer=0
while n!=0:
    digit=n%10
    if digit == 1:
        answer=answer+pow(2,i)
    n=n/10
    i+=1
print(answer)