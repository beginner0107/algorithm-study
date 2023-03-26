import sys
input = sys.stdin.readline

"""부분합문제풀이
    1. 부분합을 모두 구할 필요 없다.
    2. 최소 길이를 구해야 하기 때문에 일정부분에서 부분합이 M을 넘어간다면 다음 포인트로 넘어가도 된다.
    3. 현재 부분합을 구하려고 하는 시점이 최소길이를 넘어가면 다음 포인트로 넘어가도 된다.
    """

N, M = map(int,input().split())
lst = list(map(int,input().split()))

s, e = 0, 1 #처음과 끝
temp = lst[s] #현재까지 구간합 값
min_len = 987654321

while s < N:
    if temp >= M: #비교하려는 값보다 현재 합이 더 클때
        min_len = min(min_len, e-s) #현재 구간합 길이 저장
        
        temp -= lst[s] #구간합에서 s포인트값 빼기
        s += 1 #S 한칸 전진
        
        if temp <M and e < N:
            temp += lst[e] #e포인트 값 저장
            e += 1 #e 한칸 전진
            
    else: #temp < M 비교대상이 더 클 때
        if e >= N: #e포인트가 리스트 길이를 넘어가면 stop
            break
        
        #e포인트 저장 후 전진
        temp += lst[e]
        e += 1
        
        #현재 길이가 최소구간합길이보다 길때
        if e-s >= min_len:
            temp -= lst[s]
            s += 1
            
            
print(0 if min_len > N else min_len)
        