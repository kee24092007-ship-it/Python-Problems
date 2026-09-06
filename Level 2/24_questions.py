"""
Question 24 (Level 2): Print the first ten multiples of n, one per line.
Test case: Input: 3; Output: 3, 6, ..., 30
"""


n = int(input())
for i in range(1, 11):
    print(n * i)
