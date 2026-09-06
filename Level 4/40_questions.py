"""
Question: Print the smallest number in a space-separated list.
Testcase: Input: 2 9 4; Output: 2
"""

numbers = list(map(int, input().split()))
print(min(numbers))
