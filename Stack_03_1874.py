# 스택 > 스택 수열

# input_data = 5
input_data = int(input())

count = 1
stack = []
signs = []
chk_prob = True

for i in range(input_data):
    chk_num = int(input())

    while count<=chk_num:
        stack.append(count)
        signs.append("+")
        count+=1

    if chk_num == stack[-1]:
        stack.pop()
        signs.append("-")
    else:
        chk_prob = False
        break

if chk_prob == False:
    print("NO")
else:
    for sign in signs:
        print(sign)
    