import sys
n = int(input())    # N값 입력
nMan = []           # 음수 남자 배열
nWoman = []         # 음수 여자 배열
pMan = []           # 양수 남자 배열
pWoman = []         # 양수 여자 배열

# 남자 입력
mans = sys.stdin.readline()
mans = mans.split(' ')

# 여자 입력
womans = sys.stdin.readline()
womans = womans.split(' ')

# 양수/음수 분리
for i in range(n) :
    h = int(mans[i])
    if h > 0 :
        pMan.append(h)
    else :
        nMan.append(h)

for i in range(n) :
    h = int(womans[i])
    if h > 0:
        pWoman.append(h)
    else :
        nWoman.append(h)

# 양수 남/녀 오름차순 정렬, 음수 남/녀 내림차순 정렬
nMan.sort(reverse=True)
nWoman.sort(reverse=True)
pMan.sort()
pWoman.sort()

# 카운트, 인덱스 
cnt = 0
m_idx = 0
w_idx = 0

# -남자와 +여자 쌍
while m_idx < len(nMan) and w_idx < len(pWoman) : # 인덱스가 넘지 않으면
    if nMan[m_idx] + pWoman[w_idx] < 0 :        # 두 값이 합쳐져서 음수이면
        cnt = cnt + 1               # 쌍 증가
        m_idx = m_idx + 1           # 다음 인덱스
        w_idx = w_idx + 1           # 다음 인덱스
    else :                      # 음수가 아니면(쌍이 안이뤄질 경우)
        m_idx = m_idx + 1       # 남자 인덱스 증가

# 인덱스 초기화
m_idx = 0
w_idx = 0

# -여자와 +남자 쌍
while w_idx < len(nWoman) and m_idx < len(pMan) : # 인덱스가 넘지 않으면
    if nWoman[w_idx] + pMan[m_idx] < 0 :        # 두 값이 합쳐져서 음수이면
        cnt = cnt + 1           # 쌍 증가
        m_idx = m_idx + 1       # 다음 인덱스
        w_idx = w_idx + 1       # 다음 인덱스
    else :                      # 음수가 아니면(쌍이 이뤄지지 않을 경우)
        w_idx = w_idx + 1       # 여자 인덱스 증가

# 값 반환
print(cnt)
        

       
