n = int(input())

# 종말의 수들을 계산해 놓는다
ends = []
i = 666
while len(ends) < n:
    if '666' in str(i):
        ends.append(i)
    i = i + 1

# N번째로 작은 종말의 수 출력
print(ends[n-1])
