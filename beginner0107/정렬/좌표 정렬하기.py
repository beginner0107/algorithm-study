# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성

n = int(input()) 

li = []

for _ in range(n):
    x, y = map(int, input().split())
    li.append([x, y])

# x좌표가 같으면 y좌표가 증가하는 순서로 정렬하는 람다식
li.sort(key=lambda x: (x[0], x[1])) 

# 첫 줄부터 N개의 줄에 점을 정렬한 결과를 출력
for i in range(n):
    print(li[i][0], li[i][1])
