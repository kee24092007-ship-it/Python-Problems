"""
Question 25 (Level 1): Count the number of digits in a positive integer.
Test case: Input: 538; Output: 3
"""


n = int(input())
count = 0
while n:
    count += 1
    n //= 10
print(count)
