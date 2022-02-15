def solution(sizes):
    answer = 0
    max_w = 0
    max_h = 0

    for w in sizes:
        if w[0]<w[1]:
            temp = w[0]
            w[0] = w[1]
            w[1] = temp
    
    for w in sizes:
        if max_w < w[0]:
            max_w = w[0]
        if max_h < w[1]:
            max_h = w[1]

    answer = max_w * max_h
    
    return answer