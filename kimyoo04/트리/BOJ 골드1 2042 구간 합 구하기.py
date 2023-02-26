

"""
문제
어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

예제 입력 1
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5

예제 출력 1
17
12
"""

# 세그먼트 트리
# https://www.youtube.com/watch?v=1d9sqmuLy-o

"""
1. 트리초기화 및 트리의 크기 정하기
    - K 값 : 2^K >= N
    - 2^K * 2

2. 시작노드 인덱스 2^K 로 시작

3. 부모노드 채우기
    - 부모노드 값 = 자식 노드 2개의 합
    - 부모노드 인덱스 = 자식노드 인덱스 // 2

4. 질의값 구하기 (어디부터 어디까지의 합, 최댓값, 최솟값)
    a. 질의 index를 트리에 맞게 변경
        - 질의 index + 2^K - 1
    b. 값 선택 기준
        - start_node % 2 == 1 시 선택 후 + 1, (start_node + 1) // 2 로 오른쪽 부모노드 선택
        - end_node % 2 == 0 시 선택 후 - 1, (end_node -1) // 2 로 왼쪽 부모노드 선택
        - start_node index > end_node index 시 탈출 <- 선택한 부모노드가 교차 될 때
    c. 결과 도출
        - 구간합의 경우, 선택된 값을 모두 더하고 반환
        - 최대의 경우, 선택된 값 중에 최댓값을 반환
        - 최소의 경우, 선택된 값 중에 최솟값을 반환

5. 값 업데이트 하기
    - 구간합의 경우, 리프노드에 변경된 값을 저장 후에 변경된 값 만큼을 // 2 한 인덱스인 부모 노드에도 모두 적용

- 데이터의 변경이 없을 땐 prefix sum array 를 사용하기, 변경이 일어나면 indexed tree 사용
"""
import sys; input = sys.stdin.readline

N, M, K = map(int, input().split())  # 수의 개수, 변경이 일어나는 횟수, 구간 합을 구하는 횟수
tree_height = 0
length = N

# tree_height 값 도출
while length != 0:
    length //= 2
    tree_height += 1

tree_size = 2 ** (tree_height + 1)

# 1. 트리초기화 및 트리의 크기 정하기
tree = [0 for _ in range(tree_size)]

# 2. 시작노드 인덱스 2^K 로 시작해서 리프 노드 저장
for i in range(2 ** tree_height, 2 ** tree_height + N):
    num = int(input())
    tree[i] = num

# 3. 부모노드 채우기 (0번 인덱스 제외)
index_1 = tree_size - 1
while index_1 != 1:
    tree[index_1 // 2] += tree[index_1]
    index_1 -= 1

for _ in range(M + K):
    # a == 1, b 번째 인덱스, c 바꿀 값
    # a == 2, b 인덱스 ~ c 인덱스의 합
    a, b, c = map(int, input().split())

    # a 가 1 이면 값 업데이트
    if a == 1:
        index_2 = b + 2 ** tree_height - 1 # 실제 값을 저장한 위치
        diff = c - tree[index_2]

        while index_2 != 0:
            tree[index_2] += diff
            index_2 //= 2

    # a 가 2 이면 구간 합 구하기
    elif a == 2:
        sum_ = 0

        start_index = b + 2 ** tree_height - 1
        end_index = c + 2 ** tree_height - 1

        while start_index <= end_index:
            if start_index % 2 == 1:
                sum_ += tree[start_index]
                start_index += 1 # 오른쪽으로 이동
            if end_index % 2 == 0:
                sum_ += tree[end_index]
                end_index -= 1 # 왼쪽으로 이동
            start_index //= 2
            end_index //= 2

        print(sum_)