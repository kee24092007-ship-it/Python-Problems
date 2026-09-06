"""
Question: Find the least common multiple of two integers.
Testcase: Input: 4 6; Output: 12
"""

import math
a, b = map(int, input().split())
print(abs(a * b) // math.gcd(a, b))
