import sys
input = sys.stdin.readline

N = int(input())
sch = [list(map(int, input().split())) for _ in range(N)]

# 0. 종료시간 순으로 정렬 
sch = sorted(sch, key=lambda a: a[0])
sch = sorted(sch, key=lambda a: a[1])

last = 0 
answer = 0
for start, end in sch:
	if start >= last:
		answer += 1
		last = end
print(answer)