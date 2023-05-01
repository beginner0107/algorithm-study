def solution(n, costs):
    # find-union 사용
    # find 함수
    def find(parent, x):
        if parent[x] == x:
            return x
        parent[x] = find(parent, parent[x])
        return parent[x]

    # union 함수
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    # kruskal 알고리즘
    def kruskal(n, edges):
        parent = [i for i in range(n+1)]
        edges.sort(key=lambda x: x[2])
        mst_weight = 0
        # mst = []
        for u, v, weight in edges:
            if find(parent, u) != find(parent, v):
                union(parent, u, v)
                mst_weight = mst_weight + weight
                # mst.append((u, v, weight))
        return mst_weight
    return kruskal(n, costs)
