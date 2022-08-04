n=int(input("enter n"))
isPrime=1

for i in range(2,n):

    if (n%i == 0):
        isPrime=0
        break

if isPrime == 1:
    print(n ,"is prime")
else:
    print(n,"is not prime")