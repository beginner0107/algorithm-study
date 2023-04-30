def solution(n, wires):
    answer=int(1e9)
    
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
    
    from collections import Counter
    for flag in range(len(wires)): #전선 끊기
        for i,j in wires[:flag]+wires[flag+1:]:
            union_parent(parent,i,j) 
        for i,j in wires[:flag]+wires[flag+1:]:
            union_parent(parent,i,j) 
        
        if len(set(parent[1:]))!=2: #만약 두 개의 전선으로 나누어지지 않는다면 pass
            parent=[i for i in range(n+1)]
            continue
        
        countgroup=list(Counter(parent[1:]).values()) #각 그룹의 송전탑 개수
        
        answer=min(answer,abs(countgroup[0] - countgroup[1]))
        parent=[i for i in range(n+1)] #초기화
        
    return answer
