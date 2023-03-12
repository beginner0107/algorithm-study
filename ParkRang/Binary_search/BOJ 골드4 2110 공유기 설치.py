import sys
N, C = map(int, input().split()) # 집의 수, 공유기 수
X = []  # 집 배열

for i in range(N) :
    X.append(int(sys.stdin.readline())) # X에 집 추가

X.sort() # 집 정렬

first = 1           # 최소 거리
last = X[-1]-X[0]   # 최대 거리

while first<=last : # 이진 탐색
    count = 1       # 공유기
    mid = (first+last)//2 # 공유기 사이의 거리

    start = X[0]

    # 배열 값을 통해 설치
    for i in range(len(X)) :
        if start + mid <= X[i] :
            start = X[i]
            count = count + 1

    if count < C :      # 공유기 수에 따라 공유기 거리 감소
        last = mid - 1
    else :              # 공유기 거리 증가
        first = mid + 1

print(last)
