def solution(numbers):
    answer = 0
    sumNumber = range(0,10)
    for i in sumNumber:
        answer = answer + i
    for number in numbers:
        answer = answer - number
    return answer