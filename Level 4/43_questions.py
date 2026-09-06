"""
Question: Check whether a line of text is a palindrome ignoring case.
Testcase: Input: Level; Output: True
"""

text = input().lower()
print(text == text[::-1])
