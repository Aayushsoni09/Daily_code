n=int(input("enter n"))
prod = 1
sum = 0
while n != 0:
    digit = n % 10
    prod = prod * digit
    sum = sum + digit

    n =int(n / 10)

answer = prod - sum
print(answer)