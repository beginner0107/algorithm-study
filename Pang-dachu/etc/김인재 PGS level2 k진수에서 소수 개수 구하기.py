# https://school.programmers.co.kr/learn/courses/30/lessons/92335

from math import sqrt

def trans(n,k) :
    result = ''
    
    while n :
        result += str(n%k)
        n //= k
    
    result = result[::-1]
    return result

def prime(n) :   
    for i in range(2, int(sqrt(n)) +1 ) :
        if n % i == 0 :
            print(n," 소수 아님 ")
            return False
    print(n," 소수임 ")
    return True


def solution(n, k):
    result = 0
            
    n = trans(n, k)
    n = n.split('0')
    print( n )
    for i in n :
        if i : 
            if int(i) > 1 and prime(int(i)) :
                result += 1
            
    return result 