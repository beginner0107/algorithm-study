https://school.programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):
    number = n + 1
    
    while True :
        if bin(n)[2:].count('1') == bin(number)[2:].count('1') :
            return number
        
        number += 1
   