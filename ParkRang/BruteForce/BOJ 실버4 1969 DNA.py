# N, M 입력받기
N, M = map(int, input().split())

DNA = []
answer = ''
other = 0

# DNA 입력받기
for i in range(N) :
    DNA.append(input())

# 문자열을 세로로 먼저 검사, 값들의 양 받아옴
for i in range(M):
    A,C,G,T = 0,0,0,0
    for j in range(N) :
        if DNA[j][i] == 'A' :
            A = A+1
        elif DNA[j][i] == 'C' :
            C = C + 1
        elif DNA[j][i] == 'G' :
            G = G + 1
        elif DNA[j][i] == 'T' :
            T = T + 1

# A,C,G,T를 알파벳 순으로 우선하여 문자열에 첨가
    if max(A,C,G,T) == A :
        answer = answer + 'A'
        other = other + C + G + T
    elif max(A,C,G,T) == C :
        other = other + A + G + T
        answer = answer + 'C'
    elif max(A,C,G,T) == G :
        answer = answer + 'G'
        other = other + A + C + T
    elif max(A,C,G,T) == T :
        answer = answer + 'T'
        other = other + A + C + G

print(answer)
print(other)

    
