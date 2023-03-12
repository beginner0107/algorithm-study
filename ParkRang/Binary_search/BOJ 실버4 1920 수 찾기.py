# 이진 탐색 함수
def binary_search(array, target, start, end):
    # 이진 탐색
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return None

# 첫 배열 입력
N1 = int(input())
A1 = list(map(int, input().split()))

# 다음 배열 입력
N2 = int(input())
A2 = list(map(int, input().split()))

A1.sort()

# 반복문을 통해 배열 이진 탐색
for i in range(N2) :
    result = binary_search(A1, A2[i], 0, N1 - 1)
    if result == None :
        print(0)
    else :
        print(1)
