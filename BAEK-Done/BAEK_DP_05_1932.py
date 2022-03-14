# 동적 계획법 > 정수 삼각형

length = int(input())
dp = []

for i in range(length):
    ipt_arr = list(map(int, input().split()))
    dp.append(ipt_arr)

floor = 2
for i in range(1, length):
    for j in range(floor):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif i == j:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
    
    floor += 1

print(max(dp[length-1]))
