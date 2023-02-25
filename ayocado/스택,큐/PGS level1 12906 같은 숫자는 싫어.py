'''
● 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12906

    배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
    
    - 제한사항
    배열 arr의 크기 : 1,000,000 이하의 자연수
    배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
    
    - 입출력 예시
    [1,1,3,3,0,1,1]	-> [1,3,0,1]
    [4,4,4,3,3] -> [4,3]
    
    
● 생각
    스택을 이용한 간단한 문제
    비어있는 리스트를 생성하고, push할 숫자가 top과 같은 숫자면 push하지 않고 다음 숫자로 넘어간다.
    
'''

def solution(arr):
    stack = []
    
    for i in arr:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
    
    return stack