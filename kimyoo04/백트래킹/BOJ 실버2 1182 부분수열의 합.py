# https://www.acmicpc.net/problem/1182


"""
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 입력
5 0
-7 -3 -2 5 8
예제 출력
1
"""

import sys; input=sys.stdin.readline


N, S = map(int, input().split()) # N 사용할 숫자 개수, S 부분수열의 합
nums = list(map(int, input().split())) # nums 사용할 숫자들
n_list = [] # 중복 체크용
cnt = 0 # 부분수열의 개수


def back(start):
    global cnt

    # 배열에 값이 있으면서 부분수열의 합이면
    if n_list and sum(n_list) == S:
        cnt += 1

    for i in range(start, N):
        # if i not in n_list: # 이부분 때문에 값이 달라짐. 어차피 append 할 때, num[i] 으로 하기 때문에 없어야 함
            n_list.append(nums[i])
            back(i+1)
            n_list.pop()

    # 수열의 길이만큼 개수가 차면 return
    if len(n_list) == N:
        return


back(0)
print(cnt)


"""
# 다른 풀이

import sys; input = sys.stdin.readline
from itertools import combinations


N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

# combination 함수를 통해
for i in range(1, N+1):
    result = combinations(nums, i)
    for num in result:
        if (sum(num) == S):
            cnt += 1
print (cnt)
"""

"""
combinations 함수 반환 값 - <itertools.combinations object at 0x00000238F6149C60>
------------------------------------
combinations([-7, -3, -2, 5, 8], 1)
(-7,),
(-3,),
(-2,),
(5,),
(8,)
------------------------------------
combinations([-7, -3, -2, 5, 8], 2)
(-7, -3),
(-7, -2),
(-7, 5),
(-7, 8),
(-3, -2),
(-3, 5),
(-3, 8),
(-2, 5),
(-2, 8),
(5, 8)
------------------------------------
combinations([-7, -3, -2, 5, 8], 3)
(-7, -3, -2),
(-7, -3, 5),
(-7, -3, 8),
(-7, -2, 5),
(-7, -2, 8),
(-7, 5, 8),
(-3, -2, 5),
(-3, -2, 8),
(-3, 5, 8),
(-2, 5, 8)
------------------------------------
combinations([-7, -3, -2, 5, 8], 4)
(-7, -3, -2, 5),
(-7, -3, -2, 8),
(-7, -3, 5, 8),
(-7, -2, 5, 8),
(-3, -2, 5, 8)
------------------------------------
combinations([-7, -3, -2, 5, 8], 5)
(-7, -3, -2, 5, 8)
------------------------------------
"""