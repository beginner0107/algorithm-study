n = int(input())
qs = []     # 쿼리들의 리스트
que = []    # 모든 숫자들 저장 리스트

for _ in range(n):
    qs.append(input())      # 쿼리 저장

s = 0       # 큐의 첫번째 인덱스 저장
for q in qs:
    query = list(q.split())
    
    if query[0] == 'push':      # push X: 정수 X를 큐에 넣는 연산이다.
        que.append(query[1])
    elif query[0] == 'pop':     # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        
        if s == len(que):
            print(-1)
            continue
        
        print(que[s])
        s += 1
    elif query[0] == 'size':        # size: 큐에 들어있는 정수의 개수를 출력한다.
        print(len(que) - s)
    elif query[0] == 'empty':       # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if s >= len(que):
            print(1)
        else:
            print(0) 
    elif query[0] == 'front':       # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if s >= len(que):
            print(-1)
        else:
            print(que[s])
    elif query[0] == 'back':        # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if s >= len(que):
            print(-1)
        else:
            print(que[-1])