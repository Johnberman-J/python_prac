# 동적 계획법 > 가장 긴 증가하는 부분 수열
# LIS 동적 계획법
# dp의 핵심은 메모! > 메모해둔걸 어떻게 사용할거냐 고민해야한다!

length = int(input())
ipt_arr = list(map(int, input().split()))
dp = [0] * length

for i in range(length):
    for j in range(i):
        if ipt_arr[i] > ipt_arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))