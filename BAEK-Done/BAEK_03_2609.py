# 정수론 > 최대공약수와 최소공배수

import math


m,n = map(int, input().split())

max_common = math.gcd(m,n)
min_common = abs(m*n)//max_common

print(max_common)
print(min_common)