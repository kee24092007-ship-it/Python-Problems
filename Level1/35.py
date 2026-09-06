a, b = map(int, input().split())

sum_a = (a % 10) + (a // 100)
sum_b = (b % 10) + (b // 100)

if sum_a > sum_b:
    n = a
else:
    n = b

ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100

print(ones + tens + hundreds)