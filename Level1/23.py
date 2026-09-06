n = int(input())

ones = n % 10
tens = n // 10

digit_sum = ones + tens

print(n - 5 * (digit_sum % 2))