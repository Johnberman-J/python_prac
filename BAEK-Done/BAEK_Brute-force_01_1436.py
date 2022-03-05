# 브루트포스 > 영화감독 숌
# while 조건을 잘 생각해봐! => true는 무한루프를 유발하기 때문에 별로 좋지 않다

series_number = int(input())
title_number = 666
count = 0

while True:
    if "666" in str(title_number):
        count += 1
    
    if count == series_number:
        print(title_number)
        break
    title_number += 1
