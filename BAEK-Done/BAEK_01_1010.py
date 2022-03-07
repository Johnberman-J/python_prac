# 정수론  > 다리 놓기

import math


length = int(input())

for i in range(length):
    temp_list = list(map(int, input().split()))
    print(math.comb(temp_list[1],temp_list[0]))