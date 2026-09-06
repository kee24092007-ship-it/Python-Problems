"""
Question 21 (Level 1): Print the sum of all even integers from 1 through n.
Test case: Input: 6; Output: 12
"""


n = int(input())
print(sum(i for i in range(1, n + 1) if i % 2 == 0))
