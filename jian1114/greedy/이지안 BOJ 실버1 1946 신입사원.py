# 입력값 시간단축
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	N = int(input())
	employ = [list(map(int, input().split())) for _ in range(N)]

	# 1. 서류 전형 순위대로 정렬
	employ_sort = sorted(employ)

	# 2. 면접 젼형 순위가 합격한 지원자의 면접전형 순위보다 높으면 합격
	top = 0
	answer = 1
	for i in range(1, len(employ_sort)):
		if employ_sort[top][1] > employ_sort[i][1]:
			top = i
			answer += 1
	print(answer)