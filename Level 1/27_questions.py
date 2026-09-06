"""
Question 27 (Level 1): Check whether the given integer is a palindrome.
Test case: Input: 121; Output: Palindrome
"""


n = int(input())
print('Palindrome' if str(n) == str(n)[::-1] else 'Not palindrome')
