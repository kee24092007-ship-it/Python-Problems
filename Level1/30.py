n = int(input())

tens = (n // 10) % 10
hundreds = (n // 100) % 10

if tens + hundreds == 10 and (tens > 7 or hundreds > 7):
    print("Success")
else:
    print("Failure")