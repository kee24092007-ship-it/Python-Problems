n = int(input())

ones = n % 10
hundreds = n // 100

if ones + hundreds < 10:
    print("Success")
else:
    print("Failure")