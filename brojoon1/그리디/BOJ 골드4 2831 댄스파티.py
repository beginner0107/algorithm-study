"""
man = [[작은 여자와], [큰 여자와]]
woman = [[큰 남자와], [작은 남자와]]

"""

import sys

def dance_partner(idx):
    global answer
    i = 0
    j = 0
    
    while True:
        if (i >= len(man[idx])) or (j >= len(woman[idx])):
            break
        
        if idx == 0:
            tall = man[idx][i]
        else:
            tall = woman[idx][j]
            
        if idx == 0:
            small = woman[idx][j]
        else:
            small = man[idx][i]
        
        # 작은 사람과 춤추고 싶은 사람이 큰 사람과 춤추고 싶은 사람보다 작을 때
        # ex) 1700 / -1800 
        if tall <= small:
            if idx == 0:
                i += 1
            else:
                j += 1
        # tall > small 
        else: 
            answer += 1
            i += 1
            j += 1     
        
    # for i, j in zip(range(len(man[idx])), range(len(woman[idx]))):
        
    #     if idx == 0:
    #         tall = man[idx][i]
    #     else:
    #         tall = woman[idx][j]
            
    #     if idx == 0:
    #         small = woman[idx][j]
    #     else:
    #         small = man[idx][i]
        
    #     # 작은 사람과 춤추고 싶은 사람이 큰 사람과 춤추고 싶은 사람보다 작을 때
    #     # ex) 1700 / -1800 
    #     if tall <= small:
    #         if idx == 0:
    #             i += 1
    #         else:
    #             j += 1
    #     # tall > small 
    #     else: 
    #         answer += 1
    #         i += 1
    #         j += 1     

"""
man = [[작은 여자와], [큰 여자와]]
woman = [[큰 남자와], [작은 남자와]]
"""

N = int(sys.stdin.readline())

# 비어있는 2차원 리스트 선언
man = [[] for _ in range(2)]
woman = [[] for _ in range(2)]

man_arr = list(map(int, sys.stdin.readline().split()))
woman_arr = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    man_key = man_arr[i]
    woman_key = woman_arr[i]
    
    # man = [[작은 여자와], [큰 여자와]]
    if man_key < 0:
        man[0].append(abs(man_key))
    else:
        man[1].append(man_key)    
    
    # woman = [[큰 남자와], [작은 남자와]]
    if woman_key > 0:
        woman[0].append(woman_key)
    else:
        woman[1].append(abs(woman_key))

# 정렬       
for i in range(2):
    man[i].sort()
    woman[i].sort()

answer = 0

dance_partner(0)
dance_partner(1)

print(answer)
