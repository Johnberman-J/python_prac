# 그리디 알고리즘 > 동전 0

m,n = list(map(int, input().split()))
change_arr = []

for i in range(m):
    change = int(input())
    change_arr.append(change)

change_arr.reverse()

change_sum = 0
for change in change_arr:
    if n == 0:
        break
    if change > n:
        continue
    
    change_sum += n//change
    n %= change

print(change_sum)