"""
Question: Convert minutes into whole hours and remaining minutes.
Testcase: Input: 135; Output: 2 hours 15 minutes
"""

minutes = int(input())
print(minutes // 60, 'hours', minutes % 60, 'minutes')
