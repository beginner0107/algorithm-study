import heapq

def solution(n, works):
    # works를 힙(heap)으로 변환
    heap = []
    for work in works:
        heapq.heappush(heap, -work)  # 최대값을 뽑기 위해 음수값으로 저장

    # 가장 큰 값(top)을 꺼내서 1을 빼고 다시 힙(heap)으로 만들어줌
    while n > 0:
        top = heapq.heappop(heap)
        if top == 0:  # 더 이상 남은 작업이 없으면 종료
            break
        heapq.heappush(heap, top+1)
        n -= 1

    # works 요소의 제곱합을 반환
    return sum([work**2 for work in heap])