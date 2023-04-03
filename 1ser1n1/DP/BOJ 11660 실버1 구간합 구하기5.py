import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list_n = [[0] * (n+1)] #원본배열
list_sum = [[0] * (n+1) for _ in range(n+1)] #구간합 배열

#원본 리스트 데이터 저장
for i in range(n):
    row = [0] + [int(x) for x in input().split()]
    list_n.append(row)

#합 배열 생성
for i in range(1, n+1):
    for j in range(1, n+1):
        list_sum[i][j] = list_sum[i][j-1] +list_sum[i-1][j] - list_sum[i-1][j-1] + list_n[i][j]

#질의값 받기
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = list_sum[x2][y2] - list_sum[x1-1][y2] - list_sum[x2][y1-1] + list_sum[x1-1][y1-1]
    print(result)