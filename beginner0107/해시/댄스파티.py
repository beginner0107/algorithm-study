import sys

N = sys.stdin.readline().strip()

man = list(map(int, sys.stdin.readline().split()))
girl = list(map(int, sys.stdin.readline().split()))
man.sort()  # NlogN
girl.sort() # NlogN
man_dict = dict()
girl_dict = dict()

for i in man: # 100000 -> 10 ^ 5 -> N
    if i not in man_dict.keys():
        man_dict[i] = 1
    else:
        man_dict[i] += 1

for i in girl: # 100000 -> 10 ^ 5 -> N
    if i not in girl_dict.keys():
        girl_dict[i] = 1
    else:
        girl_dict[i] += 1
# N
cnt = 0
for m in man: # (N번 반복) 1000N -> 상수시간 제외 N
    if m > 0:
        tmp = m + 1
        while tmp <= 2500: # 1000번 반복
            if -tmp in girl_dict and man_dict[m] != 0 and girl_dict[-tmp] != 0:
                cnt += 1
                man_dict[m] -= 1
                girl_dict[-tmp] -= 1
                break
            tmp += 1
    if m < 0:
        tmp = - (m + 1)
        while tmp >= 1500:
            if tmp in girl_dict and man_dict[m] != 0 and girl_dict[tmp] != 0:
                cnt += 1
                man_dict[m] -= 1
                girl_dict[tmp] -= 1
                break
            tmp -= 1
# 최종 시간복잡도: O(N)
print(cnt)
