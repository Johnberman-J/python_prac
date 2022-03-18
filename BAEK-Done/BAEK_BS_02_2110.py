# 이분 탐색 > 공유기 설치

from itertools import count
from sys import stdin


n, c = map(int, stdin.readline().split())

wifi_set = []
for i in range(n):
    wifi_set.append(int(stdin.readline()))
wifi_set.sort()

high = wifi_set[-1] - wifi_set[0]
low = 1
answer = 0

while low <= high:
    mid = ( high + low ) // 2
    temp = wifi_set[0]
    count = 1

    for i in range(1, len(wifi_set)):
        if wifi_set[i] >= temp + mid:
            count += 1
            temp = wifi_set[i]

    if count >= c:
        low = mid + 1
        answer = mid
    else:
        high = mid -1

print(answer)