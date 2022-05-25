def fact(n):
    if n==0:
        return 1
    factorial=fact(n-1)
    return factorial*n

print(fact(5))