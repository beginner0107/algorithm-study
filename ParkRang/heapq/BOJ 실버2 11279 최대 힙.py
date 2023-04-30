import heapq, sys

heap = []
N = int(sys.stdin.readline())

for i in range(N) :
    # 값을 음수로 받아냄
    x = -int(sys.stdin.readline())

    # 0이 입력되면 가장 작은 값(음수화되었으므로 실제론 가장 큰 값) 출력 및 삭제
    if x == 0 :
        if len(heap)==0:
            print(0)
        else :
            print(-heapq.heappop(heap))
    # 아닌 경우 x를 우선순위 값에 삽임
    else :
        heapq.heappush(heap, x)
