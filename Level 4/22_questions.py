"""
Question 22 (Level 4): Print the sum of all odd integers from 1 through n.
Test case: Input: 5; Output: 9
"""


n = int(input())
print(sum(i for i in range(1, n + 1) if i % 2 != 0))
