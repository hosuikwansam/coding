"""
Question:
line_1 & line_2 are 2 string
line_2 is the reversed string of line_1, with some character being replaced
print the number of character being replaced
e.g. line_1 = "Hello World!"
     line_2 = "!dbroW alleH"
     expected output: 2 (Hello becomes Hella & World becomes Worbd)
"""

line_1 = input()
line_2 = input()
line_2 = line_2[::-1]
count = 0
for i in range(len(line_1)):
    if line_1[i] != line_2[i]:
        count += 1
print(count)
