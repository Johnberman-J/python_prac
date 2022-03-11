# 동적 계획법 > 파도반 수열

length = int(input())
dp = [0] * 100

dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3, len(dp)):
    dp[i] = dp[i-3] + dp[i-2]

for i in range(length):
    ipt = int(input())
    print(dp[ipt-1])
