# 그리디 알고리즘 > ATM

length = int(input())
ipt_data = list(map(int, input().split()))
ipt_data.sort()
total_time = 0
waiting_time = 0

for need_time in ipt_data:
    waiting_time += need_time
    total_time += waiting_time
    
print(total_time)