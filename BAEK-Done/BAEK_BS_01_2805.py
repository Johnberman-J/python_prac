# 이분 탐색 > 나무 자르기

n, m = map(int, input().split())
height_arr = list(map(int, input().split()))
start = 0
end = max(height_arr)

while start <= end:
    mid = (start + end) // 2
    sum = 0

    for height in height_arr:
        if height > mid:
            sum += height - mid

    if sum >= m :
        start = mid + 1
    else:
        end = mid - 1

print(end)