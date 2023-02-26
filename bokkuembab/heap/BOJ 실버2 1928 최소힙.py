# n: 연산의 개수, nums: 입력된 정수를 저장하는 heap
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    tmp = int(input())
    
    if tmp == 0:
        if nums:    # heap이 비어있지 않다면
            print(heappop(nums))   # heap에서 가장 작은 값 꺼냄
        else:
            print(0)    # heap이 비어있다면 0 출력
    else:    
        heappush(nums, tmp)