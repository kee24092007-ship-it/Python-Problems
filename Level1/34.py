a, b = map(int, input().split())

tens_a = (a // 10) % 10
tens_b = (b // 10) % 10

if tens_a > tens_b:
    n = a
else:
    n = b

ones = n % 10
hundreds = n // 100

print(abs(ones - hundreds))