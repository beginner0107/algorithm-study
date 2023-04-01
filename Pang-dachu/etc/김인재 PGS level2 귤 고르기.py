# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import deque
from collections import Counter

def solution(k, tangerine):
    count = 0
    
    counter = Counter(tangerine)
    
    print( counter )
    print( counter.values() )