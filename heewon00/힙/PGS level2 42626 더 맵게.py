import heapq
def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    
    while K>scoville[0]: #가장 작은 수가 K보다 커질 때까지
        if len(scoville)<=1:
            return -1
        i=heapq.heappop(scoville)
        j=heapq.heappop(scoville)
        heapq.heappush(scoville, i+j*2)
        answer+=1
    
    return answer
