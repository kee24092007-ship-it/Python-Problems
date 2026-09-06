"""
Question 26 (Level 1): Print the digits of an integer in reverse order.
Test case: Input: 120; Output: 21
"""


n = int(input())
original = n
reverse = 0
while n:
    reverse = reverse * 10 + n % 10
    n //= 10
print(reverse)
