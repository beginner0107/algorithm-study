
# 노드의 갯수
N = int(input())
# 리스트 초기화
# adj = [[] for _ in range(n)]

# 배열
T = list(map(int, input().split()))

'''
# 노드 연결
for i in range(N) :
    # adj[i].append(T[i])
    adj[T[i]].append(i)

A = True
while A :
    for i in range
'''

def dfs(node) :
    T[node] = 'X'
    for i in range(N) :
        if T[i] == node :
            dfs(i)

dfs(int(input()))
lt = 0

for i in range(N) :
    if T[i]!= 'X' and i not in T :
        lt = lt + 1

print(lt)
