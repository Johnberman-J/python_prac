# 큐 > 최대 힙
# readline으로 풀어내야 함

import heapq
import sys


length = int(input())
temp_heap = []
answers = []

for i in range(length):
    ipt_data = int(sys.stdin.readline())
    
    if ipt_data:
        heapq.heappush(temp_heap, -ipt_data)
    else:
        if temp_heap:
            pop_data = heapq.heappop(temp_heap)
            print(-pop_data)
        else:
            print(0)
