"""
Question:
Given an integer, find the longest length of 0
e.g. input: 100300040000
     expected output: 4
"""

n = input()
best_length = 0
current = 0
last_zero = False
for digit in str(n):
    if last_zero and digit == '0':
        current += 1
    elif digit == '0':
        current = 1
        last_zero = True
    elif current > best_length:
        last_zero = False
        best_length = current
    else:
        current = 0
print(max(best_length, current))

"""
Good coding from others:
import re
n = input()
s = re.findall('[0]+', n)
if s:
    print(len(max(s)))
else:
    print(0)
"""