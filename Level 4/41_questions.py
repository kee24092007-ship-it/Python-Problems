"""
Question: Sort a space-separated list in ascending order.
Testcase: Input: 3 1 2; Output: 1 2 3
"""

numbers = list(map(int, input().split()))
print(*sorted(numbers))
