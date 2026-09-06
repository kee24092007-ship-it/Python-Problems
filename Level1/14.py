n = int(input())

ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100

print(ones * 100 + tens * 10 + hundreds)