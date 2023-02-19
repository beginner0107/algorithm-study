import sys; input=sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        input()

    # 가장 적은 종류의 비행기(간선)를 타고 모든 국가(노드)들을 여행하는 방법은 노드 수의 - 1 이다.
    print(N - 1)