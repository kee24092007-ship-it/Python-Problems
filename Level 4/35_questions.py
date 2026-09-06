"""
Question: Check whether a year is a leap year.
Testcase: Input: 2024; Output: True
"""

year = int(input())
print(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
