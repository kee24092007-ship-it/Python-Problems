n = int(input())

ones = n % 10
hundreds = n // 100

print(n - 5 * (ones == hundreds))