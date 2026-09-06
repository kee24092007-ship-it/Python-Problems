n = int(input())

tens = (n // 10) % 10
hundreds = (n // 100) % 10

if tens + hundreds > 10:
    print("Success")
else:
    print("Failure")