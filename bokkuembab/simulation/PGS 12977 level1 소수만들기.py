# itertools의 combinations 함수를 사용하지 않고, 직접 구현하는 것을 연습하기 위해 풀어봄!

# combination 함수 구현
def combination(arr, n):
    
    res = []  # 결과를 담을 리스트
    
    if n == 0:   # 0개를 고른다면, 빈 행렬 출력
        return [[]]
    
    for i in range(len(arr) - n + 1):  # 더 이상 n개를 고를 수 없을 때까지 순회
        ele = arr[i]   # 시작 요소 넣기
        for rest in combination(arr[i + 1:], n - 1):
            res.append([ele] + rest)
            
    return res

# 소수 확인 함수 구현
def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def solution(nums):
    ans = 0
    
    for snums in [sum(c) for c in combination(nums, 3)]:
        ans += is_prime(snums)
        
    return ans