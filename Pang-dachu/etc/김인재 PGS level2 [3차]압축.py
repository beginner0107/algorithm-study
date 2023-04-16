# https://school.programmers.co.kr/learn/courses/30/lessons/17684

from collections import deque 

def solution(msg):
    answer = []
    # 초기 사전 생성 
    dict = {}
    for i in range(65,91) :
        dict[chr(i)] = ( i - 64 )
    ##
    word_q = deque(msg)

    while word_q :
        alpha = word_q.popleft()

        try : 
            while True : 

                if alpha in dict.keys() :
                    beta = word_q.popleft()
                    alpha += beta
                else :
                    dict[alpha] = max(dict.values())+1
                    word_q.extendleft(alpha[-1])
                    answer.append(dict[alpha[:-1]])
                    break

        except IndexError : 
            answer.append(dict[alpha])
            break

    return answer