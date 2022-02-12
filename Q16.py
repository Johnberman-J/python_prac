from tabnanny import check


def solution(s):
    answer = True
    chk_str = s.lower()
    count = 0

    for word in chk_str:
        if word == "p":
            count = count + 1
        elif word == "y":
            count = count - 1
    
    if count != 0:
        answer = False
    else:
        answer = True

    return answer