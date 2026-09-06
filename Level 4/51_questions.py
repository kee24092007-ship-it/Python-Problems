"""
Question: Replace every vowel in a line with an asterisk.
Testcase: Input: hello; Output: h*ll*
"""

text = input()
print(''.join('*' if ch.lower() in 'aeiou' else ch for ch in text))
