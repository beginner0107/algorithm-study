# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0
    
    for alpha, beta in zip( sorted(A) , sorted(B, reverse=True) ):
        answer += (alpha * beta) 

    return answer