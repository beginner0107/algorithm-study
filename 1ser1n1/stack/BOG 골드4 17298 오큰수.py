import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

answer = [0] * N
bucket = []

for i in range(N):
    while bucket and A[bucket[-1]] < A[i] :#오큰수 조건
        answer[bucket.pop()] = A[i] #정답 리스트에 오큰수 저장

    bucket.append(i)

#오큰 수가 없는 인덱스에 -1저장
while bucket:
    answer[bucket.pop()] = -1

print(" ".join([str(i) for i in answer]))