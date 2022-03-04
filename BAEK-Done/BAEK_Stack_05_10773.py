# 스택 > 제로

length = int(input())
stack = []

for i in range(length):
    ipt_data = int(input())
    if ipt_data == 0:
        stack.pop()
    else:
        stack.append(ipt_data)

sum = 0

for number in stack:
    sum += number

print(sum)