import sys
from collections import deque


def bfs(start, target):
    visited = [0] * 200001        # 순간이동은 2배의 위치로 이동 -> 순간이동을 통해 방문할 수 있는 노드 번호 범위는 현재 위치의 2배
    visited2 = [False] * 200001
    # 3가지의 경우 앞으로 한칸 가거나
    # 뒤로 한칸 가거나
    # 순간이동 하기 2 * X
    q = deque([start])
    while q:
        v = q.popleft()
        visited2[v] = True
        front, back, teleport = v + 1, v - 1, v * 2
        for idx, i in enumerate([teleport, back, front]):  # 순서가 중요, 순간이동 -> 뒤로 -> 앞으로 순으로 해야 함
            if 200000 >= i >= 0 and not visited2[i]:       # 범위 안에 있고, 방문하지 않은 경우
                if visited[i] == 0:
                    if idx == 0:                           # 순간이동을 했다
                        visited[i] = visited[v]
                    else:                                  # 뒤로가거나 앞으로 가거나
                        visited[i] = visited[v] + 1
                    q.append(i)
                    if target == i:                        # 동생의 위치와 같다면
                        return visited[i]


start, target = map(int, sys.stdin.readline().split())
if start == target:
    print(0)
else:
    print(bfs(start, target))
