# https://www.acmicpc.net/problem/15650

"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력
3 1
예제 출력
1
2
3
"""

"""
핵심
- 중복되는 것은 제외시키는 방식 (Combination, 조합)
"""

import sys; input=sys.stdin.readline


def back(start):
    if len(n_list) == M:
        print(" ".join(map(str, n_list)))
        return

    # start를 통해 앞의 숫자가 뒤보다 크도록 설정
    for i in range(start, N+1):
        if i not in n_list:
            n_list.append(i)
            back(i+1)
            n_list.pop()


# N 사용할 숫자 수, M 배열의 길이
N, M = map(int, input().split())
n_list = []

back(1)


"""
[다른 사례]

from itertools import combinations

N, M = map(int, input().split())
numList = [i for i in range(1, N+1)]

for seq in combinations(numList, M):
    print(*seq)
"""