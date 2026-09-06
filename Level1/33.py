a, b = map(int, input().split())

if a > b:
    n = a
else:
    n = b

print(n // 10 + n % 10)