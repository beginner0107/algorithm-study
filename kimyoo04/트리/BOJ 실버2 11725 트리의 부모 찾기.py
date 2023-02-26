# https://www.acmicpc.net/problem/11725

"""
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1
7
1 6
6 3
3 5
4 1
2 4
4 7

예제 출력 1
4
6
1
3
1
4
"""

import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**6) # 반복제한 해제

n = int(input())
# 방문 여부 파악
visited = [0 for _ in range(n+1)]

# 인접 리스트 방식 사용
tree = [[] * (n) for _ in range(n+1)]
for _ in range(n-1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

def dfs(root):
    for i in tree[root]:
        if visited[i] == 0:
            # 방문한 노드에 부모 노드를 할당
            visited[i] = root
            dfs(i)

dfs(1)

# 2 부터 n 까지 부모 노드 출력
for i in range(2,n+1):
    print(visited[i])