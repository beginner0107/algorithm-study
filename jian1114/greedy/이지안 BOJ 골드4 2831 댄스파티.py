N = int(input())

boys = list(map(int, input().split()))
girls = list(map(int, input().split()))

boys_n = sorted([boy for boy in boys if boy < 0], reverse=True)
boys_p = sorted([boy for boy in boys if boy > 0])
girls_n = sorted([girl for girl in girls if girl < 0], reverse=True)
girls_p = sorted([girl for girl in girls if girl > 0])

# 두 리스트 모두 존재할 때
cnt = 0 
while boys_p and girls_n:
    # 가장 키 큰 남자와 가장 키가 작은 여자와 더하기
    if boys_p[-1] + girls_n[-1] < 0:
        cnt += 1
        boys_p.pop()
        girls_n.pop()
    # 가장 키 큰 남자와 가장 키가 작은 여자와 더했는데 양수인 경우
    # 즉, 해당 남자보다 키가 큰 여자가 없기 때문에 쌍을 이룰 수 없음
    else:
        boys_p.pop()

# 위 방법과 동일
while boys_n and girls_p:
    if boys_n[-1] + girls_p[-1] < 0:
        cnt += 1
        boys_n.pop()
        girls_p.pop()
    else:
        girls_p.pop()
print(cnt)