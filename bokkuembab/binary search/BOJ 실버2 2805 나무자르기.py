import sys
input = sys.stdin.readline

n, target = map(int, input().split())   # n: 나무의 수, target: 가져가려는 나무의 길이
trees = list(map(int, input().split()))    # 모든 나무의 길이 리스트

low, high = 1, max(trees)
while low <= high:
        mid = (low + high) // 2
        
        getT = 0   
        for l in trees:    # 지정 길이로 잘랐을 때 남는 길이 계산
            if l > mid:
                getT += (l - mid) 
        
        if getT < target:    # 가져갈 수 있는 길이가 목표보다 적으면, 자르는 길이 짧게 하기
            high = mid - 1
        elif getT >= target:    # 가져갈 수 있는 길이가 목표보다 크면, 자르는 길이 길게 하기
            low = mid + 1

print(high)