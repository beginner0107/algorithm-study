def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        # if i == 0:
        #     answer.append(arr[i])
        
        # arr 스택에 해당 원소가 없으면 원소 추가
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    
    return answer