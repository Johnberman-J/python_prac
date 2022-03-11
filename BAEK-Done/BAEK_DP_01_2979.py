# 동적 계획법 > 계단 오르기

length = int(input())
score = [0]*300

for i in range(length):
    score[i] = int(input())

dp = [0]*300
dp[0] = score[0]
dp[1] = max(score[0]+score[1], score[1])
dp[2] = max(score[0]+score[2], score[1]+score[2])

for i in range(3, length):
    dp[i] = max(score[i]+dp[i-2], score[i]+score[i-1]+dp[i-3])

print(dp[length-1])
