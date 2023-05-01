'''
from collections import deque

def solution(numbers, target):
    answer=0
    queue=deque()
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    
    while queue:
        temp, idx = queue.popleft()
        idx+=1
        if idx<len(numbers):
            queue.append([temp+numbers[idx],idx])
            queue.append([temp-numbers[idx],idx])
        else:
            if target==temp:
                answer+=1   
    return answer
'''
def solution(numbers,target):
    if not numbers and target==0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0])+\
    solution(numbers[1:],target+numbers[0])
