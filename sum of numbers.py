def sumno(n):
    if n==0:
        return 0
    sum=sumno(n-1)
    return sum+n

print(sumno(5))