import heapq, sys

N = int(sys.stdin.readline())

lectures = []
heap = []
room = []

for i in range(N) :
    lectures.append(list(map(int, sys.stdin.readline().split())))    

lectures.sort(key=lambda x: x[1])  # 시작 시간을 기준으로 정렬

for lect in lectures:
    # 가장 빨리 끝나는 강의가 끝나고, 현재 강의를 시작 가능하면
    if len(heap) > 0 and heap[0] <= lect[1]:
        heapq.heappop(heap)  # 해당 강의실에서 강의 끝
    else:  # 아니면 강의실 추가
        room.append([])

    heapq.heappush(heap, lect[2])  # 해당 강의실에 현재 강의를 추가
    room[-1].append(lect[2])  # 강의실 목록에 강의 추가

print(len(room))
