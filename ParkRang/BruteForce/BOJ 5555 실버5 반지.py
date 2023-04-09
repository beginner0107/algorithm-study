# 입력받을 문자열
s = input()

# 반지 수
N = int(input())

# 반지의 문자열 배열
ring = []
cnt = 0

# 반지의 문자열 입력
for i in range(N) :
    ring.append(input())

# 앞뒤로 3번씩 입력해서 검사
for i in range(N) :
    ring[i] = ring[i] * 3
    if s in ring[i] :
        cnt = cnt + 1

print(cnt)
