"""
Question: Print the first n terms of the Fibonacci sequence.
Testcase: Input: 5; Output: 0 1 1 2 3
"""

n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
