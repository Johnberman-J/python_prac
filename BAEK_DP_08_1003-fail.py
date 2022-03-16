# 동적 계획법 > 피보나치 함수

length = int(input())
dp = []
dp[0] = 0
dp[1] = 1

for i in range(length):
    fibo = int(input())
    dp[fibo] = dp[fibo-1] + dp[fibo-2]