# https://school.programmers.co.kr/learn/courses/30/lessons/12946

answer = []

def hanoi(n, a, b, c) :
    if n == 1 :
        answer.append( [a,c] )
    
    else : 
        hanoi( n-1, a, c, b )
        answer.append( [a,c] )
        hanoi( n-1, b, a, c )


def solution(n):
    hanoi(n, 1, 2, 3)
    return answer