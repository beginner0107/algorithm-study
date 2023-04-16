import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())    # 연산 개수
h_list = []    # 절댓값 힙

for _ in range(n):
    x = int(input())    # 값 입력 받음
    
    if x == 0:    # 힙에서 값 삭제 및 출력하기
        if h_list:    # 리스트에 값이 존재한다면,
            print(heappop(h_list)[1])    # 절댓값이 가장 작은 값 pop
        else:     # 리스트가 비어있다면,
            print(0)
    else:    # 힙에 값 넣어주기
        heappush(h_list, (abs(x), x))    # (절댓값, 원본값) 형태로 넣어주기