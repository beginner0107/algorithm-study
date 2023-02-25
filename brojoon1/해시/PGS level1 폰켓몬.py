"""
(N/2)마리를 뽑을 때, 중복되는 포켓몬이 없다면 (N/2) 종류의 포켓몬 선택
중복 포켓몬이 존재한다면 중복 제외한 종류 수 = 최대 종류 수
"""

def solution(nums):
    answer = 0
    
    # set을 이용해 포켓몬 중복 삭제
    poket_set = set(nums)
    
    return min(len(poket_set), len(nums)//2)