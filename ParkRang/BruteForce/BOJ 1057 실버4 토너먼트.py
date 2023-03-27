# 인원수, 번호 입력
n, a, b = map(int, input().split())

# 라운드 번호
rounds = 0

# 상위 라운드 진행
while a != b:
    rounds += 1
    a, b = (a+1)//2, (b+1)//2
    
print(rounds)
