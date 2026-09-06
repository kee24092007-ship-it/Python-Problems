"""
Question: Calculate the perimeter of a rectangle from its length and width.
Testcase: Input: 4 5; Output: 18
"""

length, width = map(int, input().split())
print(2 * (length + width))
