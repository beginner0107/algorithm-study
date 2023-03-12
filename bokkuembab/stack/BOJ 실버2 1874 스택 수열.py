import sys
input = sys.stdin.readline

n = int(input())    # 정수의 개수
nums = []     # 수열리스트
stack = []    # 스택
ans = []
for _ in range(n):    # 수열 입력받기
    nums.append(int(input()))
    
id = 0
for i in range(1, n + 1):
    stack.append(i)
    ans.append('+')
    
    if stack[-1] > nums[id]:    # 꺼낼 수 없는 수이면, 실패
        break

    while stack[-1:] == nums[id:id+1]:
        ans.append('-')
        stack.pop()
        id += 1
        
        if id >= n:    # 끝까지 다 뺐으면, 나오기
            break

if stack:    # 스택에서 숫자를 모두 꺼내지 못했으면, 실패
    print('NO')
else:
    for i in ans:
        print(i)