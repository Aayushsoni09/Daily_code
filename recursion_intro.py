def hello(n):
    if n==0:
        return
    print("hello",n)
    hello(n-1)
hello(10)
