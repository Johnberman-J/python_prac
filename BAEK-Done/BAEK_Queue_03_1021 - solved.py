# 큐 > 회전하는 큐

import sys


n, m = list(map(int, sys.stdin.readline().split()))
number_arr = list(map(int,sys.stdin.readline().split()))

circular_queue = list(range(1, n+1))
sum = 0

for number in number_arr:
    while True:
        if circular_queue.index(number) == 0:
            circular_queue.pop(0)
            break
        if abs(circular_queue.index(number) - 0) <= abs(circular_queue.index(number) - len(circular_queue)):
            # 절대값(거리의 차이) 를 비교 후 왼쪽으로 갈지 오른쪽으로 갈지 판단
            circular_queue.append(circular_queue.pop(0))
        else:
            circular_queue.insert(0, circular_queue.pop())
        sum += 1

print(sum)
