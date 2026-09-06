n = int(input())

tens = n // 10
ones = n % 10

if tens + ones == 10:
    print("Success")
else:
    print("Failure")