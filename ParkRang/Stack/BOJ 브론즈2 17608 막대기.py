import sys
stack = []			#스택 리스트 선언
T = 0
N = int(sys.stdin.readline())	#int(input()) 시간초과
for i in range(N) :
    num = int(sys.stdin.readline())	#막대기 길이 입력
    if num >= T :			#최대보다 크면 최대값 지정
        T = num
    j=len(stack)			#앞의 값들과 비교 위함
    while j>0 and stack[j-1]<=num :	#리스트 순서가 0보다 크고 이전 스택이 작으면
        stack.pop()			#값 제거
        j = j-1			#하나씩 비교
    stack.append(num)		#비교 이후 스택에 추가

print(len(stack))