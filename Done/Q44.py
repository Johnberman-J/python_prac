from fractions import gcd

def solution(n, m):
    answer = []

    commonMax = gcd(n,m)
    commonMin = (n*m)//commonMax
    
    answer.append(commonMax)
    answer.append(commonMin)

    return answer


