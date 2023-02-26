# 시간 복잡도 O(n * m) -> O(len(discount) * len(want))
def solution(want, number, discount):
    answer = 0
    w_num = dict()
    for i in range(len(want)):
        w_num[want[i]] = number[i]

    for i in range(len(discount)):
        li = discount[i:i + 10]
        isOk = True
        for j in range(len(want)):
            if w_num[want[j]] > li.count(want[j]):
                isOk = False
                break
        if isOk:
            answer += 1
    return answer