#import sys
#input = sys.stdin.readline

N = int(input())
stack = []        # 현재 stack
answer = []       # + - 
no = False        # NO

current_num = 1       
for _ in range(N):
    num = int(input())

    # 입력한 수를 만날때까지 오름차순으로 계속 push
    while current_num <= num:
        stack.append(current_num)
        answer.append("+")  
        current_num += 1
    
    # stack의 마지막 숫자가 num이라면 pop 아니라면 NO 출력
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        no = True
    
if no == True:
    print("NO")
else:
    for i in answer:
        print(i)
        
# 출력할 때 print(answer)을 해버리면 출력초과가 뜨기 때문에 아래 방법들을 사용해야 한다.
# for문을 이용해 하나씩 출력하는 방법 
# print("\n".join(answer))