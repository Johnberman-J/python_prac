# 브루트포스 > 분해 합

ipt_number = int(input())

for i in range(1, ipt_number+1):
    construct_num = sum((map(int, str(i)))) + i

    if construct_num == ipt_number:
        print(i)
        break
    if i == ipt_number:
        print(0)
