def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

# def solution(n):
#     answer = ""
#     while n>0:
#         n, mod = divmod(n,3)
#         answer += str(mod)
#     return int(answer, 3)
