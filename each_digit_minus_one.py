"""
Question:
Given some input and expected output, guess and write the function
Input   Output
2       1
52      41
3072    21061
1112    1
71891   678
"""
i = input()
answer = []
for digit in i:
    modified = int(digit) - 1
    if modified > 0:
        answer.append(modified)
    if modified < 0:
        answer.append(10)
print(int("".join([str(integer) for integer in answer])))
