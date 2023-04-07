n,m = map(int, input().split())

def find_parent(parent, x):
    if x!=parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
   
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]

graph=[]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c,a,b))

graph.sort()

result = 0
last = 0

for i in graph:
    c, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        # 작은 마을부터 연결
        union_parent(parent, a, b)
        result += c
        last = c

print(result - last)
