N = int(input())        # 첫째줄 입력

H = list(map(int, input().split())) # 입력 값
dart = [0] * 1000001                # 다트의 높이 카운트 배열

cnt = 0                 # 다트의 수

for i in range(N) :
    if dart[H[i]] == 0 :                # 다트가 안 맞았다면 다트 추가, 다트 높이 하락
        dart[H[i]-1] = dart[H[i]-1] + 1
        cnt = cnt + 1
    else :                              # 다트가 맞았다면 다트 높이 하락
        dart[H[i]] = dart[H[i]] - 1
        dart[H[i]-1] = dart[H[i]-1] + 1

print(cnt)

# cnt를 모두 제거, print(sum(dart)) 해도 가능
# 이럴 경우 코드는 
'''
N = int(input())

H = list(map(int, input().split()))
dart = [0] * 1000001

for i in range(N) :
    if dart[H[i]] == 0 :
        dart[H[i]-1] = dart[H[i]-1] + 1
    else :
        dart[H[i]] = dart[H[i]] - 1
        dart[H[i]-1] = dart[H[i]-1] + 1

print(sum(dart))
'''
