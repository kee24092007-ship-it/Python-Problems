n = int(input())

s = (n // 100) + ((n // 10) % 10) + (n % 10)

while s >= 10:
    s = (s // 10) + (s % 10)

print(s)