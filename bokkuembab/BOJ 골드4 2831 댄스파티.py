# 양수 -> 자신보다 키가 큰 사람 선호
# 음수 -> 키가 작은 사람 선호
nums = int(input())    # 남자, 여자 각각 n명
mli = list(map(int, input().split()))
wli = list(map(int, input().split()))

mli.sort(key=lambda x: abs(x))
wli.sort(key=lambda x: abs(x))

# 둘을 곱했을 때 음수이고, 더했을 때도 음수인 경우를 찾아야 함.
# 둘을 곱했을 때 양수이고, 