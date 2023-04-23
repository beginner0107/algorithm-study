import sys
input = sys.stdin.readline
from heapq import heappush, heappop
# python의 heapq는 최소힙 기준이므로, 최대힙 구현하려면 -를 붙여 넣어주면 됨!

n = int(input())    # 연산 횟수 입력 받기
heap = []    # 힙 생성
for _ in range(n):
    x = int(input())
    if x > 0:     # x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산
        heappush(heap, -x)    # 최대힙 구현하기 위해 (-) 붙여서 넣어주기
    else:    # x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우
        if heap:    # 힙에 요소가 있다면,
            print(-heappop(heap))    # 음수로 넣어줬으므로, (-) 붙여서 출력
        else:     # 힙에 요소가 없다면,
            print(0)