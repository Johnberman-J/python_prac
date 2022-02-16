import math

def solution(nums):
    answer = 0
    length = len(nums)
    sum_nums = - 0
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                sum_nums = nums[i]+nums[j]+nums[k]
                sqrt_sum = int(math.sqrt(sum_nums))+1


                for now in range(2, sqrt_sum):
                    if sum_nums % now == 0: break
                    elif now == sqrt_sum-1:
                        answer += 1
    return answer