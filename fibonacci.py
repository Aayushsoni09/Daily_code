def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 1;
    partial1=fibo(n-1)
    partial2=fibo(n-2)
    return partial1+partial2

print(fibo(6))
