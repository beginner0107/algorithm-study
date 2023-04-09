from collections import deque

def bfs(start, end, increment):
    queue = deque([start])
    visited = [0 for _ in range(end + 1)]

    while queue:
        node = queue.popleft()
        one_step = node + increment
        two_step = node * 2
        three_step = node * 3

        for i in [one_step, two_step, three_step]:
            if i <= end and visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)
    return visited[end]


def solution(x, y, n):
    if x == y: 
        return 0
    answer = bfs(x, y, n)
    if answer == 0:
        return -1
    return answer