# 이분 탐색 > K번째 수

size = int(input())
idx = int(input())
start = 1
end = idx

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(1, size+1):
        count += min(mid//i, size)

    if count >= idx:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)