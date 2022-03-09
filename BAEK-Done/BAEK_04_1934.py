# 정수론 > 최소공배수

import math


length = int(input())

for i in range(length):
    m,n = map(int, input().split())
    max_common = math.gcd(m, n)
    min_common = abs(m*n)//max_common
    print(min_common)