n = int(input())

tens = (n // 10) % 10
hundreds = (n // 100) % 10

print(n - 5 * (tens == hundreds))