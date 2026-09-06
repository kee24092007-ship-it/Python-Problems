n = int(input())

ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100

if ones + tens + hundreds == 10:
    print("Success")
else:
    print("Failure")