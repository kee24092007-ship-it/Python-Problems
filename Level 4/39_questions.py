"""
Question: Print the largest number in a space-separated list.
Testcase: Input: 2 9 4; Output: 9
"""

numbers = list(map(int, input().split()))
print(max(numbers))
