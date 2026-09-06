"""
Question 13 (Level 1): Classify an integer as Positive, Negative, or Zero.
Test case: Input: -2; Output: Negative
"""


n = int(input())
print('Positive' if n > 0 else 'Negative' if n < 0 else 'Zero')
