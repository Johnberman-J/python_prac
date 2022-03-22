# 이분 탐색 > 가장 긴 증가하는 부분 수열

length = int(input())
ipt_nums = list(map(int, input().split()))
ans_arr = [0]

for ipt_num in ipt_nums:
    if ans_arr[-1] < ipt_num:
        ans_arr.append(ipt_num)
    else:
        left = 0
        right = len(ans_arr)

        while left < right:
            mid = (left + right) // 2
            
            if ans_arr[mid] < ipt_num:
                left = mid + 1
            else:
                right = mid
            
            ans_arr[right] = ipt_num

print(len(ans_arr)-1)
