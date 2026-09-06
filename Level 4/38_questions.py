"""
Question: Count the vowels in a line of text.
Testcase: Input: hello; Output: 2
"""

text = input().lower()
print(sum(ch in 'aeiou' for ch in text))
