"""
Question 23 (Level 4): Compute n factorial.
Test case: Input: 5; Output: 120
"""


n = int(input())
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(factorial)
