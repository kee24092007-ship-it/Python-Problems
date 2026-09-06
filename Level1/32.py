a, b = map(int, input().split())

if a + b < 100:
    print(a + b)
else:
    print(abs(a - b))