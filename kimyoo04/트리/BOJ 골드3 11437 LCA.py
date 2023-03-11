# https://www.acmicpc.net/problem/11437

"""
문제
N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.

두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

입력
첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다. 그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

예제 입력 1
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15

예제 출력 1
2
4
2
1
3
1
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(100000)

N = int(input())
tree = [[] for _ in range(N + 1)]


# 간선 수 N-1
for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)


parent = [0 for _ in range(N + 1)]
depth = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]


# 부모노드와 트리깊이 구하기
def dfs(node, tree_depth):
    visited[node] = True
    depth[node] = tree_depth

    for end_node in tree[node]:
        if not visited[end_node]:
            parent[end_node] = node # 부모노드 저장
            dfs(end_node, tree_depth + 1) # 트리깊이 전달


dfs(1, 0)


def lca(A, B):
    # 깊이 먼저 일치시키기
    while depth[A] != depth[B]:
        # 트리깊이가 깊은 노드를 부모노드로 이동
        if depth[A] > depth[B]:
            A = parent[A]
        else:
            B = parent[B]

    # 두 노드의 값이 일치하지 않으면 두 노드의 부모노드로 이동
    while A != B:
        A = parent[A]
        B = parent[B]

    return str(A)


M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    print(lca(A, B))
    print("\n")



"""
bfs 방법
"""
from collections import deque

def bfs(start):
    # queue 생성
    queue = deque([start])
    visited[start] = True

    # 트리깊이, 해당 트리깊이의 노드개수, 방문한 노드 초기화
    tree_depth = 1
    node_num = 1
    cnt = 0

    # 그래프가 끝날 때까지
    while queue:
        node = queue.popleft()

        for end_node in tree[node]:
            # 해당 노드를 방문한 적이 없다면
            if not visited[end_node]:
                queue.append(end_node)
                visited[end_node] = True

                # 해당 노드의 부모노드와 트리깊이 저장
                parent[end_node] = node
                depth[end_node] = tree_depth

        cnt += 1
        if cnt == node_num:
            # 트리깊이 + 1
            tree_depth += 1
            # 노드개수, 방문한 노드 초기화
            node_num = len(queue)
            cnt = 0


"""
시간초과 해결이 안돼서 dfs, bfs 방식과 다른 것으로 할 예정. pypy3 는 통과
"""

