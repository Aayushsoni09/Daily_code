def sum(n):
    if n==0:
        return 0
    leftpart=n//10
    rightpart=n%10
    return sum(leftpart)+rightpart

print(sum(5213))