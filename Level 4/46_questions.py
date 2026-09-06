"""
Question: Find the greatest common divisor of two integers.
Testcase: Input: 12 8; Output: 4
"""

import math
a, b = map(int, input().split())
print(math.gcd(a, b))
