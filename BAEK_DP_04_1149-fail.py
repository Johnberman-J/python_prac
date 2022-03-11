# 동적 계획법 > RGB 거리
# 세가지의 누적합을 전부 dp에 넣어두고 최소값을 마지막에 찾아낸다!

length = int(input())
dp = []
sum = 0

for i in range(length):
    ipt_arr = list(map(int, input().split()))
    sum += min(ipt_arr)
    dp.append(ipt_arr.index(min(ipt_arr)))
