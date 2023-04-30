# https://www.acmicpc.net/problem/11724

"""
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1
6 5
1 2
2 5
5 1
3 4
4 6

예제 출력 1
2
"""

import sys; input=sys.stdin.readline; sys.setrecursionlimit(10000)

# N 정점의 개수, M 간선의 개수
N, M = map(int, input().split())

# 인접리스트 생성
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    # uv 간선의 양 끝점
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 방문노드
visited = [False] * (N + 1)

# 연결 요소 개수
count = 0

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)