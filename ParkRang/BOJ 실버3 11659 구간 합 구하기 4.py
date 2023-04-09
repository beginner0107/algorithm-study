N, M = map(int, input().split())

# 입력값 받기
numbers = list(map(int, input().split()))
k = [0,numbers[0]]
answer = []

# 앞의 숫자들을 합친 채 저장
for i in range(1,len(numbers)) :
    k.append(k[i] + numbers[i])

# 값을 받아올 때 앞에  숫자를 뺀 값을 저장하여 가져옴
for i in range(M) :
    n1, n2 = map(int, input().split())
    answer.append(k[n2]-k[n1-1])

for i in range(M):
    print(answer[i])
