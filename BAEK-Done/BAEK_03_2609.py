# 정수론 > 최대공약수와 최소공배수
# "/"는 연산 결과가 float 형태로 나타냄
# "//"는 연산 결과가 int 형태로 나타냄

import math


m,n = map(int, input().split())

max_common = math.gcd(m,n)
min_common = abs(m*n)//max_common

print(max_common)
print(min_common)