# 큐 > 최소 힙

import heapq
import sys


length = int(input())
min_heap = []

for i in range(length):
    input_num = int(sys.stdin.readline())

    if input_num > 0:
        heapq.heappush(min_heap, input_num)
    else:
        if len(min_heap) > 0:
            pop_number = heapq.heappop(min_heap)
            print(pop_number)
        else:
            print(0)
        