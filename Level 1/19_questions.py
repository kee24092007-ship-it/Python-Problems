"""
Question 19 (Level 1): Print the larger of two integers using a conditional expression.
Test case: Input: 8 5; Output: 8
"""


a, b = map(int, input().split())
print(a if a > b else b)
