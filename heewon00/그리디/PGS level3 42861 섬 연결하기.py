def solution(n, costs):
    answer = 0
    
    def find_parent(parent, x):
        if parent[x]!=x:
            parent[x]=find_parent(parent,parent[x])
        return parent[x]
    
    def union_parent(parent,a,b):
        a=find_parent(parent,a)
        b=find_parent(parent,b)
        
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
    
    parent=[i for i in range(n+1)]
    costs.sort(key=lambda x:x[2])
    
    for x,y,cost in costs:
        if find_parent(parent,x)!=find_parent(parent,y):
            union_parent(parent,x,y)
            answer+=cost
    
    return answer
