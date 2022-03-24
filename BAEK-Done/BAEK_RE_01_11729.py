# 재귀 함수 > 하노이 탑 이동 순서

import math


def move_circle(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    move_circle(n-1, start, 6-start-end)
    print(start, end)
    move_circle(n-1, 6-start-end, end)
    
n = int(input())
print(int(math.pow(2,n)-1))
move_circle(n, 1, 3)