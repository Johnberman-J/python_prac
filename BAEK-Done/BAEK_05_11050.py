# 정수론 > 이항계수1

import math


m,n = map(int, input().split())

binomial_num = math.comb(m, n)
print(binomial_num)