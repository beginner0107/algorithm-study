"""
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

예제 입력 1
10 15
5 1 3 5 10 7 4 9 2 8

예제 출력 1
2
"""

import sys; input=sys.stdin.readline

# 시간초과가 난 풀이

# 입력값 받기
n, s = map(int, input().split())
num_list = list(map(int, input().split()))

# 필요한 변수 초기화
sum_list = [0]
temp = 0
flag = 1

# 합 배열 만들기
for num in num_list:
    temp = temp + num
    sum_list.append(temp)

# i 슬라이딩 윈도우 크기
for i in range(1, n+1):
    # j 슬라이딩 할 인덱스
    for j in range(0, n-i+1):
        # print('j+i, j', j+i, i)
        # print(sum_list[j+i] - sum_list[j])
        if sum_list[j+i] - sum_list[j] > s:
            print(i)
            exit()

if flag:
    print(0)


# 답안 확인


import sys; input=sys.stdin.readline

# 입력값 받기
n, s = map(int, input().split())
num_list = list(map(int, input().split()))

# 필요한 변수 선언
left, right = 0, 0 # 두 개의 포인터
sum_ = 0 # 합을 저장할 변수
min_length = sys.maxsize # 정답을 담을 변수

while True:
    # 오른쪽으로 윈도우 축소
    if sum_ >= s:
        min_length = min(min_length, right - left)
        sum_ -= num_list[left]
        left += 1
    elif right == n:
        break
    # 오른쪽으로 윈도우 확장
    else:
        sum_ += num_list[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)