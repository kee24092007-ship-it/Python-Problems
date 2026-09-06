"""
Question: Print a right triangle of stars with n rows.
Testcase: Input: 3; Output: *, **, ***
"""

n = int(input())
for i in range(1, n + 1):
    print('*' * i)
