import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = str(input())
    
    cnt = 0
    for s in S:

        # ( 인 경우는 무조건 cnt + 1
        if s == '(':
            cnt += 1

        # ) 인 경우, 우선 cnt - 1을 한 뒤, 만약 cnt가 음수가 된다면 ( 가 없었다는 뜻이므로 NO를 출력
        elif s == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    
    # cnt = 0인 경우, 즉 ( 와 ) 가 딱 맞아떨어진 경우는 YES
    if cnt == 0:
        print("YES")

    # cnt가 양수인 경우, 즉 ( 개수가 더 많은 경우는 NO 출력 
    elif cnt > 0:
        print('NO')
