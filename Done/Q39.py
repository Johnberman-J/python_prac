def solution(s, n):
    lower = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    
    for char in s:
        if char in lower:
            idx = lower.find(char)+n 
            answer += lower[idx%26]
        elif char in upper:
            idx = upper.find(char)+n
            answer += upper[idx%26]
        else: 
            answer += " "
            
    return answer