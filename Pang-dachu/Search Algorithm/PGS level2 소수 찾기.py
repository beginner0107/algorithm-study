from itertools import permutations
import math 

def prime_number(x) :
    if x < 2 : 
        return 0
    
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return 0
    return 1

def solution(numbers):
    num = list(numbers)
    cnt = 0
    
    permu = []
    
    for i in range(1, len(num)+1) :
        permu += list(permutations(num,i))
    
    permu = list( set([int(''.join(x)) for x in permu]) )
    
    for i in permu :
        cnt += prime_number(i)
    
    return cnt 
    