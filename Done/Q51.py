def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        decoded1 = decoder(n, arr1[i])
        decoded2 = decoder(n, arr2[i])
        temp_arr = []
        for j in range(len(decoded1)):
            if decoded1[j] == "0" and decoded2[j] == "0":
                temp_arr.append(" ")
            else:
                temp_arr.append("#") 
        answer.append("".join(temp_arr))

    return answer


def decoder(digit, number):
    decoded_arr = list(str(bin(number)[2:]))
    length_difference = digit - len(decoded_arr)

    for i in range(length_difference):
        decoded_arr.insert(i,"0")

    return decoded_arr
