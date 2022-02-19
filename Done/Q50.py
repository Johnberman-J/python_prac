def solution(nums):
    answer = 0
    max_pick = int(len(nums)/2)
    pocket_set = set()

    for i in range(len(nums)):
        pocket_set.add(nums[i])
    
    pocekt_set_size = pocket_set.__len__()

    if pocekt_set_size <= max_pick:
        answer = pocekt_set_size
    else:
        answer = max_pick

    return answer