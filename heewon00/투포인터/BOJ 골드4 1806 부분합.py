n,s=map(int,input().split())
numlst = list(map(int,input().split()))

l,r=0,0 
temp=0

inf=1e9
ans=inf

while True:
    if temp >= s :
        ans = min( ans, r-l )
        temp -= numlst[l] 
        l+=1

    elif r==n: break

    else:
        temp += numlst[r]
        r+=1

print(0) if ans==inf else print(ans)
